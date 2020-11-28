#!/bin/bash

# """
# # Для программной реализации
# ps aux > ps.out
# head -n 1 ps.out > sorted.ps
# tail -n +2 ps.out | sort -k1,2 >> sorted.ps

# cut -d ' ' -f 1 sorted.ps | uniq # список пользователей
# cut -d ' ' -f 1 sorted.ps | uniq | wc -l  # количество уникальных пользователей

# tail -n +2 sorted.ps | grep '^root\s' > root.ps  # выбрать всех пользователей по имени

# # обрамление тегом
# cat root.ps | sed 's/^/<li>/' > root.html
# sed -i 's/$/<\/li>/' root.html

# # считаем итог
# echo '<p><b>Итого процессов: NN</p></b>' > total.root
# sed -i 's/NN/$(cat root.html | wc -l)/' total.root
# """

SORTED="sorted_ps.tmp"
SEP="<hr noshade>"
INDEX="index.html"

echo -e "<html>\n<title>Статистика процессов</title>\n<body><h1>Распределение процессов по пользователям</h1>" > "$INDEX"


ps aux | tail -n +2 | sort -k1,2 | sed "s/</\&lt;/" | sed "s/>/\&gt;/" > $SORTED

users="$( < $SORTED sed "s/\s.*//" | uniq )"

mapfile -t users <<< "$users"

summary=0
for user in "${users[@]}"
do     
    tmp_user="$user.tmp"
    # tail -n +2 "$SORTED" | grep "^$user\s" | sed "s/^/<li>/" | sed "s/$/<\/li>/" > "$tmp_user"
    cat "$SORTED" | grep "^$user\s" | sed "s/^/<li>/" | sed "s/$/<\/li>/" > "$tmp_user"

    tmp_total="$user-total.tmp"
    total=$(< "$tmp_user" wc -l )
    echo "<p><b>Итого процессов: $total</b></p>" > "$tmp_total"
    
    summary=$(( summary+total ))

    {
        echo "$SEP"
        echo "<h3>$user</h3>"
        cat "$tmp_user"
        echo "$SEP"
        cat "$tmp_total"
    } >> "$INDEX"
    
    rm "$tmp_user"
    rm "$tmp_total"
done

rm "$SORTED"
echo "<h3>Итог: $summary</h3>" >> "$INDEX"
echo -e "</body>\n</html>" >> "$INDEX"
