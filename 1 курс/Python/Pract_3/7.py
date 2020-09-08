# -*- coding: utf-8 -*-
s = input('Введите список через пробел ')
s = list(s.split(' '))
a = list()
try:
    for i in range(len(s)):
        x=int(s[i])
except: print("Проверьте правильность ввода данных")
else:
    for i in range(len(s)):
        if s[i] not in a:
            a.append(s[i])
    for i in range(len(a)):
        print(a[i], end = " ")