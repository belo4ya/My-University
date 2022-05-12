import socket
from typing import Any


def port_validation(value: Any, check_open: bool = False) -> bool:
    try:
        value = int(value)
        if 1 <= value <= 65535:
            if check_open:
                return check_port_open(value)
            print(f"Корректный порт {value}")
            return True

        print(f"Некорректное значение {value} для порта")
        return False

    except ValueError:
        print(f"Значение {value} не является числом!")
        return False


def check_port_open(port: int) -> bool:
    try:
        sock = socket.socket()
        sock.bind(("", port))
        sock.close()
        print(f"Порт {port} свободен")
        return True
    except OSError:
        print(f"Порт {port} занят")
        return False


def ip_validation(address: str) -> bool:
    error_message = f"Некорректный ip-адрес {address}"
    ok_message = f"Корректный ip-адрес {address}"
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            print(error_message)
            return False
        return address.count(".") == 3
    except socket.error:
        print(error_message)
        return False

    print(ok_message)
    return True
