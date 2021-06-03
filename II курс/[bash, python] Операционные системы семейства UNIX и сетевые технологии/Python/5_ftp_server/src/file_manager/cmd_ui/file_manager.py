import cmd
import os

from src.file_manager.core.manager import Manager, Answer
from src.file_manager.core.parser import Parser
from src.file_manager.utils import get_abspath


class FileManager(cmd.Cmd):

    def __init__(self, root: str = None):
        super(FileManager, self).__init__()
        self.intro = "Добро пожаловать в простой кроссплатформенный awesome файловый менеджер. " \
                     "Введи help или ? для получения списка команд.\n"

        self.root = root or get_abspath(os.getcwd())
        self.prompt = self._prompt()
        self.out_prompt = "--- "
        self.err_prompt = "*** "

        self._executor = Manager(str(self.root))
        self._parser = Parser()

    def default(self, line: str) -> bool:
        print(self.err_prompt + f"Неопознанный синтаксис: {line}. "
                                f"Введи help или ? для получения списка доступных команд.")
        return False

    def precmd(self, line: str) -> str:
        return line if line != "~" else "root"

    def postcmd(self, stop: bool, line: str) -> bool:
        self.prompt = self._prompt()
        return stop

    def do_root(self, args):
        """
        Перейти в корневой каталог.
        Коротка форма команды: '~'.
        """
        paths, args = self._parser.parse(args)

        if self._unexpected_args(0, args):
            return

        self._on_answer(self._executor.root())

    def do_ls(self, args):
        """
        Отобразить содержимое DIR (по умолчанию текущий каталог).

        Использование
        -------------
            ls [DIR] [MASK]
            DIR - имя каталога, содержимое которого будет отображено.
            MASK - паттерн для фильтрации файлов. Возможные значения: *, ?, [seq], [!seq].
        """
        paths, args = self._parser.parse(args)
        path = paths[0] if len(paths) > 0 else ""
        mask = paths[1] if len(paths) > 1 else ""

        if self._unexpected_args(0, args):
            return

        answer = self._executor.listdir(path, mask)
        if answer.returncode == 0:
            return self.columnize([p.name for p in answer.payload])
        return self._error_handler(answer.error)

    def do_cd(self, args):
        """
        Изменить текущий каталог на DIR.

        Использование
        -------------
            cd [DIR]
            DIR - имя каталога в который будет выполнен переход.
            Для перехода на уровень вверх возможно использование синтаксиса:
            cd '.' * n, где (n - 1) - число переходов.
        """
        paths, args = self._parser.parse(args)
        path = paths[0] if paths else ""

        if self._unexpected_args(0, args):
            return

        self._on_answer(self._executor.change_dir(path))

    def do_mkdir(self, args):
        """
        Создать каталог DIR, если он еще не существует.

        Использование
        -------------
            mkdir <DIR> [options]
            DIR - имя каталога, который будет создан.

        Параметры
        ---------
            -p - создавать родительские директории при необходимости.
            -q - игнорировать оповещение о том, что каталог уже существует.
        """
        paths, args = self._parser.parse(args)
        path = paths[0] if paths else ""

        if self._unexpected_args(2, args):
            return

        self._on_answer(self._executor.create_dir(path, args))

    def do_rmdir(self, args):
        """
        Удалить DIR.

        Использование
        -------------
            rmdir <DIR> [options]
            DIR - имя каталога, который будет удален.

        Параметры
        ---------
            -r - удалить директорию вместе с её содержимым.
        """
        paths, args = self._parser.parse(args)
        path = paths[0] if paths else ""

        if self._unexpected_args(1, args):
            return

        self._on_answer(self._executor.remove_dir(path, args))

    def do_mkfile(self, args):
        """
        Создать FILE, если он еще не существует.

        Использование
        -------------
            mkfile <FILE> [options]
            FILE - имя файла, который будет создан.

        Параметры
        ---------
            -q - игнорировать оповещение о том, что файл уже существует.
        """
        paths, args = self._parser.parse(args)
        path = paths[0] if paths else ""

        if self._unexpected_args(1, args):
            return

        self._on_answer(self._executor.create_file(path, args))

    def do_rmfile(self, args):
        """
        Удалить FILE.

        Использование
        -------------
            rmfile <FILE> [options]
            FILE - имя файла, который будет удален.

        Параметры
        ---------
            -q - игнорировать оповещение о том, что файл не найден.
        """
        paths, args = self._parser.parse(args)
        path = paths[0] if paths else ""

        if self._unexpected_args(1, args):
            return

        self._on_answer(self._executor.remove_file(path, args))

    def do_write(self, args):
        """
        Записать DATA в FILE (если файл не существует, создать).

        Использование
        -------------
            write <FILE> [DATA]
            FILE - имя файла, в который будут записаны данные.
            DATA - текст для записи в файл. Для сохранения пробелов используйте "" или ''.
        """
        paths, args = self._parser.parse(args)
        path = paths[0] if len(paths) > 0 else ""
        data = paths[1] if len(paths) > 1 else ""

        if self._unexpected_args(0, args):
            return

        self._on_answer(self._executor.write_file(path, data))

    def do_dog(self, args):
        """
        Отобразить содержимое FILE.

            Использование
            -------------
            dog <FILE>
            FILE - имя файла, содержимое которого будет отображено.
        """
        paths, args = self._parser.parse(args)
        path = paths[0] if paths else ""

        if self._unexpected_args(0, args):
            return

        answer = self._executor.show_file(path)
        answer.msg = answer.payload
        self._on_answer(answer)

    def do_cp(self, args):
        """
        Скопировать SRC файл/каталог в DST каталог или файл с новым именем.

            Использование
            -------------
            cp <SRC> <DST> [options]
            SRC - имя каталога или файла, который будет скопирован.
            DST - имя целевого каталога или новое имя копируемого файла/каталога.

            Параметры
            ---------
            -r - рекурсивное копирование каталога со всем содержимым.
        """
        paths, args = self._parser.parse(args)
        src = paths[0] if len(paths) > 0 else ""
        dst = paths[1] if len(paths) > 1 else ""

        if self._unexpected_args(1, args):
            return

        self._on_answer(self._executor.copy(src, dst, args))

    def do_mv(self, args):
        """
        Переименовать SRC в DST или переместить SRC в DST (каталог).

            Использование
            -------------
            mv <SRC> <DST>
            SRC - имя каталога или файла, который будет перемещен.
            DST - имя целевого файла/каталога или новое имя для SRC файла/каталога.
        """
        paths, args = self._parser.parse(args)
        src = paths[0] if len(paths) > 0 else ""
        dst = paths[1] if len(paths) > 1 else ""

        if self._unexpected_args(0, args):
            return

        self._on_answer(self._executor.move(src, dst))

    def do_rename(self, args):
        """
        Переименовать SRC в DST.

            Использование
            -------------
            rename <SRC> <DST>
            SRC - имя каталога или файла, который будет переименован.
            DST - новое ися каталога или файла.
        """
        paths, args = self._parser.parse(args)
        src = paths[0] if len(paths) > 0 else ""
        dst = paths[1] if len(paths) > 1 else ""

        if self._unexpected_args(0, args):
            return

        self._on_answer(self._executor.rename(src, dst))

    def do_exit(self, args):
        """
        Завершить работу программы.
        """
        print("\nAwesome файловый менеджер завершил свою работу с кодом выхода 0")
        return True

    def _unexpected_args(self, expected, args) -> bool:
        if len(args) > expected:
            self._stderr("Неожиданный(-е) аргумент(-ы): {}".format("'" + "', '".join(args[expected:]) + "'"))
            return True

        return False

    def _on_answer(self, answer: Answer):
        if answer.returncode == 0:
            return self._stdout(answer.msg)
        return self._error_handler(answer.error)

    def _stdout(self, msg: str):
        if msg:
            print(self.out_prompt + msg)

    def _stderr(self, msg: str):
        if msg:
            print(self.err_prompt + msg)

    def _error_handler(self, error):
        self._stderr(str(error))

    def _prompt(self):
        cwd = os.getcwd()
        return cwd[cwd.find(self.root.name):] + "::-> "
