import argparse
from crontab import CronTab

# cron
cron = CronTab(user="belo4ya")

# аргументы коммандной строки
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--save", type=str, default="/home/belo4ya/",
                    help="Директория, бэкап которой будет производиться")
parser.add_argument("-d", "--dir", type=str, default="/home/belo4ya/backup/",
                    help="Директория для хранения бэкапов")
parser.add_argument("-m", "--minutes", type=int, default=60 * 2,
                    help="Частота архивации в минутах")
parser.add_argument("-i", "--ignore", type=str,
                    help="Файлы, которые не нужно сохранять\n"
                         "*Синтаксис регулярных выражений модуля re")
args = parser.parse_args()


if __name__ == '__main__':
    for job in cron:
        if job.comment == "inc_backup":
            cron.remove(job)
            cron.write()

    if args.ignore is None:
        job = cron.new(command="/usr/bin/python3 /home/belo4ya/PycharmProjects/incremental_archiving/inc_backup.py " +
                       f"-s {args.save} -d {args.dir} -m {args.minutes} >/dev/null 2>&1",
                       comment="inc_backup")
    else:
        job = cron.new(command="/usr/bin/python3 /home/belo4ya/PycharmProjects/incremental_archiving/inc_backup.py " +
                       f"-s {args.save} -d {args.dir} -m {args.minutes} -i {args.ignore} >/dev/null 2>&1",
                       comment="inc_backup")
    job.minute.every(args.minutes)
    print(job)
    cron.write()
