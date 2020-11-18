#!/bin/bash

SCRIPT="$HOME/bin/date.sh"
CHECKSUM="0226142b803397c760b47829f47de38b"
TASK="* * * * * $SCRIPT >/dev/null 2>&1"

IFS="  " read -r -a sum <<< "$(md5sum $SCRIPT)"
if [ "${sum[0]}" = "$CHECKSUM" ]
then
    echo "Контрольные суммы совпадают!"
    crontab -l > mycron
    echo "$TASK" >> mycron
    crontab mycron
    rm mycron
    echo "Задача: $TASK успешно создана!"
else
    echo "Контрольные суммы не совпадают!"
    echo "Задача не создана!"
fi
