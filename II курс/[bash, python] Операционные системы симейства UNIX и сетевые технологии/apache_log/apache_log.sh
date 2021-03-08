#!/bin/bash

filename="log.txt"
const_output="<time> <timezone> с хоста <host> по протоколу <http_protocol> был выполнен запрос типа <http_method> для получения реурса, находящегося по ссылке <url>. Код ответа на запрос от сервера: <http_code>. "
empty_body_output="Такой ответ не предполагает наличия тела ответа (<body_size_output>). "
body_size_output="оличество переданных байт - <response_size>"
empty_refer_output="Запрос выполнялся напрямую, а не по ссылке с другого сайта (<refer_output>). "
refer_output="оле реферер - <refer>"
client_output="Клиент использовал для обращения: <client>."

while IFS=$'\n' read -r line
do  
    output=""
    host=$(echo "$line" | grep -o '^[^ ]*')
    date=$(echo "$line" | grep -o '\[.*\]' | sed -e "s/\[//" -e "s/\]//")

    IFS=' ' read -r -a date <<< "$date"
    time="${date[0]}"                              # дата и время
    timezone="${date[1]}"                          # метка пременной зоны

    IFS='"' read -r -a double_q <<< "$line"
    request="${double_q[1]}"
    response="${double_q[2]}"
    refer="${double_q[3]}"                         # ссылка-реферер
    client="${double_q[5]}"                        # информация о клиенте

    IFS=' ' read -r -a request <<< "$request"
    http_method="${request[0]}"                    # тип запроса
    url="${request[1]}"                            # url запроса
    http_protocol="${request[2]}"                  # версия HTTP протокола

    IFS=' ' read -r -a response <<< "$response"
    http_code="${response[0]}"                     # код HTTP ответа
    response_size="${response[1]}"                 # размера тела ответа в байтах
    
    output=$(echo "$const_output" | sed -e "s|<time>|$time|" -e "s/<timezone>/$timezone/" -e "s/<host>/$host/")
    output=$(echo "$output" | sed -e "s|<http_protocol>|$http_protocol|" -e "s/<http_method>/$http_method/" )
    output=$(echo "$output" | sed -e "s|<url>|$url|" -e "s/<http_code>/$http_code/" )

    if [ "$response_size" = "-" ]
    then
        response_size="0"
        tmp_body_size_output=$(echo "$body_size_output" | sed -e "s/<response_size>/$response_size/" -e "s/^/к/" -e "s/$//")
        output+=$(echo "$empty_body_output" | sed "s/<body_size_output>/$tmp_body_size_output/")
    else
        tmp_body_size_output=$(echo "$body_size_output" | sed -e "s/<response_size>/$response_size/" -e "s/^/К/" -e "s/$/. /")
        output+=$tmp_body_size_output
    fi

    if [ "$refer" = "-" ]
    then
        refer="пустое"
        tmp_refer_output=$(echo "$refer_output" | sed -e "s/<refer>/$refer/" -e "s/^/п/" -e "s/$//")
        output+=$(echo "$empty_refer_output" | sed "s/<refer_output>/$tmp_refer_output/")
    else
        tmp_refer_output=$(echo "$refer_output" | sed -e "s|<refer>|$refer|" -e "s/^/П/" -e "s/$/. /")
        output+=$tmp_refer_output
    fi

    output+=$(echo "$client_output" | sed "s|<client>|$client|")

    # echo "$output" >> decrypted_log.txt
    echo "$output"
    echo ""

done < "$filename"
