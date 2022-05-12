import logging
import os
import random
import socket
from datetime import datetime
from time import mktime
from typing import Tuple
from wsgiref.handlers import format_date_time

import configparser


from validators import port_validation, check_port_open

LOGGER_FILE = "./logs/log.txt"

logging.basicConfig(
    format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)
logger.addHandler(logging.FileHandler(LOGGER_FILE))
config = configparser.ConfigParser()
config.read('config.ini')
config = config['MAIN']


def get_date() -> str:
    now = datetime.now()
    stamp = mktime(now.timetuple())
    return format_date_time(stamp)


class SimpleRequest:

    def __init__(self, data: bytes):
        lines = []

        for d in data.decode("utf8", "replace").split("\n"):
            line = d.strip()
            if line:
                lines.append(line)

        self.method, self.path, self.http_version = lines.pop(0).split(" ")
        self.info = {k: v for k, v in (line.split(": ") for line in lines)}

    def __str__(self) -> str:
        return f"<SimpleRequest {self.method} {self.path} {self.http_version}>"

    __repr__ = __str__


class LocaleSocket:
    """Класс для работы с сокетами"""

    def __init__(self, host="", port=80, buffer_size=1024, max_queued_connections=5):
        self._connection = None
        self._socket = None
        self.host = host
        self.port = port
        self.buffer_size = int(buffer_size)
        self.max_queued_connections = max_queued_connections

    def __repr__(self) -> str:
        status = "closed" if self._socket is None else "open"
        return f"<{status} ServerSocket {self.host}:{self.port}>"

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def open(self):
        assert self._socket is None, "ServerSocket уже открыт"
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self._socket.bind((self.host, self.port))
        except Exception:
            self.close()
            raise
        else:
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def close(self):
        assert self._socket is not None, "Данный ServerSocket уже был закрыт"
        if self._connection:
            self._connection.close()
            self._connection = None
        self._socket.close()
        self._socket = None

    def listen(self) -> Tuple[SimpleRequest, str]:
        assert (self._socket is not None), "ServerSocket должен быть открыт для получения данных"
        self._socket.listen(self.max_queued_connections)
        self._connection, address = self._socket.accept()
        data = self._connection.recv(self.buffer_size)
        return SimpleRequest(data), address[0]

    def send(self, data: bytes):
        assert self._socket is not None, "ServerSocket должен быть открыт для ответа"
        self._connection.send(data)
        self._connection.close()


class WebServer:
    """Класс сервера"""

    STATUSES = {
        200: "Ok",
        404: "File not found",
        403: "Forbidden"
    }

    def __init__(self, config: dict, port: int = 80):
        """
        Инициализирует сервер

        port    -- порт, на котором разворачивается
        homedir -- домашняя директория
        """
        self.socket = LocaleSocket(port=port, buffer_size=int(config["buffer_size"]))
        self.homedir = os.path.abspath(config["homedir"])

    def start(self):
        """Запуск web-сервера"""
        self.socket.open()
        logger.info(f"Запустили web-сервер на порту {self.socket.host}:{self.socket.port}, директория {self.homedir}")
        while True:
            self.new_client_request()

    def stop(self):
        """Приостановка работы web-сервера"""
        self.socket.close()

    def router(self, path: str) -> Tuple[bytes, int, str]:
        """Роутер для ассоциации между путями и файлами"""

        allowed_extensions = ["js", "html", "css", "png", "jpg"]

        router_dict = {
            "/": "index.html",
            "/index.html": "index.html",
            "/index": "index.html",
            "/bad": "BadRequest.page",
            "/image": "image.jpg"
        }

        # Если такой маппинг действительно существует
        if path in router_dict:

            # Имя файла, которое запрашиваем
            file_name = router_dict[path]
            # Если это разрешенное имя файла
            if file_name.split(".")[1] in allowed_extensions:
                path_str = os.path.join(self.homedir, file_name)
                with open(path_str, "rb") as f:
                    return f.read(), 200, ''
            # Ошибка 403
            else:
                with open(os.path.join(self.homedir, "403.html"), "rb") as f:
                    return f.read(), 403, "text/html"

        # Если ничего подобного нет, то 404
        else:
            with open(os.path.join(self.homedir, "404.html"), "rb") as f:
                return f.read(), 404, "text/html"

    def new_client_request(self):
        """"Обработка запроса клиента"""
        cli_request, ip_addr = self.socket.listen()
        path = cli_request.path
        # Получаем результат существования файла от роутера
        body, status_code, mime = self.router(path)
        header = self.get_header(status_code, body, mime)
        self.socket.send(header.encode() + body)
        logger.info(
            f"{get_date()} -> {ip_addr}, {path} {status_code} - {cli_request.method}")

    def get_header(self, status_code: int, body: str, mime: str):
        return "\n".join(
            [
                f"HTTP/1.1 {status_code} {self.STATUSES[status_code]}",
                f"Content-Type: {mime}",
                f"Date: {get_date()}",
                f"Content-length: {len(body)}",
                "Connection: close"
                "Server: MyServer" "\n\n",
            ]
        )


def main():
    # Чтение конфигурации сервера
    default_port = config["default_port"]
    port_input = input("Введите номер порта для сервера -> ")
    # Тут проверка на то, занят ли порт
    port_flag = port_validation(port_input, check_open=True)

    if not port_flag:

        port_input = default_port
        # Если порт по-умолчанию уже занят, то перебираем свободные порты
        if not check_port_open(default_port):
            logger.info(
                f"Порт по умолчанию {default_port} уже занят! Подбираем рандомный порт.."
            )
            stop_flag = False
            current_port = None
            while not stop_flag:
                current_port = random.randint(49152, 65535)
                logger.info(f"Сгенерировали рандомный порт {current_port}")
                stop_flag = check_port_open(current_port)

            port_input = current_port
        logger.info(f"Выставили порт {port_input} по умолчанию")

    web_server = WebServer(config=config, port=int(port_input))
    web_server.start()
    web_server.stop()


if __name__ == "__main__":
    main()
