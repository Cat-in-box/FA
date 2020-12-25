#!/bin/bash

ps -aux > ps.out

sort ps.out > sorted.ps

splitter='<hr noshade>'
body='<html><head><meta charset="utf-8"><title>Статистика процессов</title></head><body><h1>Распределение процессов по пользователям</h1><div class="row"><div class="col-12">'
footer='</div></div></body></html>'
echo $body > index.html

for CURRENT_USER in $(cat sorted.ps | awk '{print $1}' | uniq)
do

    cat sorted.ps | grep $CURRENT_USER > $CURRENT_USER.ps
    sed -e "s/$/<li> $/g" $CURRENT_USER.ps > $CURRENT_USER.html
    PROC_COUNT=$(cat $CURRENT_USER.html | wc -l)
    echo "<p><b>Итого процессов: $PROC_COUNT</b></p>" > $CURRENT_USER.total
    echo $splitter $(cat $CURRENT_USER.total) "Пользователь $CURRENT_USER" $splitter $(cat $CURRENT_USER.html) >> index.html

done

echo $footer >> index.html
echo "Complete"