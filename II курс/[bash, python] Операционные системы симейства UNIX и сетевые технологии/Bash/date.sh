#!/bin/bash

# cron:
# * * * * * /home/belo4ya/bin/date.sh  # создание файла с текущим временем в директории ~/tmp/


DATE="$(date  +%H-%M-%S)"
echo "$DATE" > "$HOME/tmp/$DATE.txt"
find "$HOME/tmp/" -maxdepth 1 -type f -mmin +17 -exec rm {} \;
