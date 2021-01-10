#!/bin/bash

# Сценарий должен вывести (на stdout) все числа,
# делящиеся на 12, в диапазоне от первого параметра до последнего.
# Если параметры заданы некорректно, скрипт должен вывести сообщение.

is_digit(){
    re='^[+-]?[0-9]+$'
    if ! [[ $1 =~ $re ]]
    then
        return 1
    else
        return 0
    fi
}

start=$1
end=$2

is_digit "$start"
start_is_digit=$?
is_digit "$end"
end_is_digit=$?
if [[ $start_is_digit != 0 || $end_is_digit != 0 ]];
then
    echo "Аргумент не является целым числом!"
    exit 1
fi

for (( i="$start";i<"$end";i++ ))
do
    if [[ $(( i % 12 )) == 0 ]]
    then
        echo "$i"
    fi
done
