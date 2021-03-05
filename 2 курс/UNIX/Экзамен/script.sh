#!/bin/bash

    #Если не было передано название файла
    if [ $(($#)) -ne 1 ]; then
        echo "Нет списка файлов!" >&2
        exit 1
    fi

    FILENAME=$1
    #Проверка на существование файла
    if [ -f "$FILENAME" ]; then
        echo "$FILENAME существует."
        
        #Читаем данные из файла
        n=1
        while read line; do
        # Читаем каждую строку из файла
            echo "Распаковка архива №$n: $line"
            if [ -f $line ] ; then
              case $line in
                 *.tar.bz2) tar xvjf $line ;;
                 *.tar.gz) tar xvzf $line ;;
                 *.tar.xz) tar xvJf $line ;;
                 *.bz2) bunzip2 $line ;;
                 *.rar) unrar x $line ;;
                 *.gz) gunzip $line ;;
                 *.tar) tar xvf $line ;;
                 *.tbz2) tar xvjf $line ;;
                 *.tgz) tar xvzf $line ;;
                 *.zip) unzip $line ;;
                 *.Z) uncompress $line ;;
                 *.7z) 7z x $line ;;
                 *.xz) unxz $line ;;
                 *.exe) cabextract $line ;;
                 *) echo "\`$line': Unknown method of file compression" ;;
              esac
           else
              echo "\`$line' no foud"
           fi

            n=$((n+1))
        done < $FILENAME
    
    else 
        echo "Файла $FILENAME не существует."
    fi
