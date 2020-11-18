#!/bin/bash

# cron:
# * * * * * /home/belo4ya/bin/date.sh >/dev/null 2>&1  # создание файла с текущим временем в директории ~/tmp/


DATE="$(date  +%H-%M-%S)"
echo "$DATE" > "$HOME/tmp/$DATE.txt"
find "$HOME/tmp/" -type f -mmin +17 -exec rm {} \;
