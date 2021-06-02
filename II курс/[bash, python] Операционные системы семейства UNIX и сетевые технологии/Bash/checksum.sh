#!/bin/bash


backup_file="$HOME/tmp/passwd.backup"
passwd_file="/etc/passwd"
if [ -e "$backup_file" ]  # проверка существует файла
then
    IFS="  " read -r -a sum_1 <<< "$(md5sum $backup_file)"  # преобразование строки в массив
    IFS="  " read -r -a sum_2 <<< "$(md5sum $passwd_file)"
    if [ "${sum_1[0]}" = "${sum_2[0]}" ]
    then
        echo "файл $passwd_file не изменился!"
        exit 0
    else
        echo "файл $passwd_file был изменен!"
        echo "обновляю копию $backup_file"
        cp -p "$passwd_file" "$backup_file"
        echo "$backup_file обновлен!"
    fi
else
    echo "$backup_file не найден!"
    echo "копирование файла $passwd_file в $backup_file"
    cp -p "$passwd_file" "$backup_file"
    echo "копирование успешно!"
fi
