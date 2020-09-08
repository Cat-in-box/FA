# -*- coding: utf-8 -*-
s = input('Введите список через пробел ')
s = list(s.split(' '))
try:
    for i in range(len(s)):
        x=int(s[i])
except: print("Проверьте правильность ввода данных")
else:
    k = 0
    for i in range(len(s)):
        if (s.count(s[i]))==1:
            k+=1
    print("Различных значений ", k)