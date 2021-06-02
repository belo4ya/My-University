#!/bin/bash

menu_list="====== MENU ======\n
a. текущий пользователь\n
b. объем используемой памяти\n
c. объем дискового пространства\n
d. запущенные процессы\n
e. процессы, запущенные текущим пользователем\n
f. системная дата и время\n
g. время запуска системы\n
h. выход\n"

line="start"
echo -e "$menu_list"
while [ "$line" != "h" ]
do
  read -s line
  echo -e "$menu_list"
  case "$line" in 
    a) echo -e "\e[31m" "$USERNAME" "\e[0m\n";;
    b) echo -e "\e[31m" "$(free)" "\e[0m\n";;
    c) echo -e "\e[31m" "$(df -h)" "\e[0m\n";;
    d) echo -e "\e[31m" "$(ps -ea)" "\e[0m\n";;
    e) echo -e "\e[31m" "$(ps -a)" "\e[0m\n";;
    f) echo -e "\e[31m" "$(date  +%d.%m.%Y\ %H:%M:%S)" "\e[0m\n";;
    g) echo -e "\e[31m" "$(uptime -s)" "\e[0m\n";;
    h) echo -e "\e[31m" "bye!" "\e[0m\n";;
  esac
done
