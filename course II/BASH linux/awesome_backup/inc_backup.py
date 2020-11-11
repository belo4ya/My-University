import os
import tarfile
import datetime
import logging
import argparse
import re

# логгирование
logger = logging.getLogger()
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%H:%M:%S"))
logger.addHandler(ch)

# аргументы коммандной строки
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--save", type=str, default="/home/belo4ya/",
                    help="Директория, бэкап которой будет производиться")
parser.add_argument("-d", "--dir", type=str, default="/home/belo4ya/backup/",
                    help="Директория для хранения бэкапов")
parser.add_argument("-m", "--minutes", type=int, default=60 * 24,
                    help="Частота архивации в минутах")
parser.add_argument("-i", "--ignore", type=str,
                    help="Файлы, которые не нужно сохранять\n"
                         "*Синтаксис регулярных выражений модуля re")
args = parser.parse_args()


def is_modified(filename, time_span):
    modified_time = os.path.getmtime(filename)
    modified_time = datetime.datetime.fromtimestamp(modified_time)
    return (datetime.datetime.now() - modified_time).seconds < time_span


def backup_dir_create(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        logging.info(f"Директория {dirname} создана")


def inc_backup(backup_dir, target_dir, time_span, ignore=None):
    now = datetime.datetime.strftime(datetime.datetime.now(), "%H:%M_%d-%m-%y")
    backup_file = os.path.join(backup_dir, "backup_" + now + ".tar.gz")

    with tarfile.open(backup_file, "w:gz") as archive:
        for root, dirs, files in os.walk(target_dir):
            for file in files:

                filename = os.path.join(root, file)
                try:
                    if is_modified(filename, time_span) and not filename == backup_file:

                        if ignore is None or ignore == "" or re.fullmatch(ignore, file):
                            archive.add(filename)
                            logging.info(f"Добавлен файл: {filename}")
                            logging.info(f"Файл изменен: {datetime.datetime.fromtimestamp(os.path.getmtime(filename))}")

                except IOError:
                    logging.info(f"Произошла ошибка: {filename}")


if __name__ == '__main__':
    target_dir = args.save
    backup_dir = args.dir
    time_span = args.minutes * 60
    ignore = args.ignore

    backup_dir_create(backup_dir)
    inc_backup(backup_dir, target_dir, time_span, ignore)
