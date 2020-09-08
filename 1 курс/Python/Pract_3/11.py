# -*- coding: utf-8 -*-
s = input('Введите список через пробел ')
s = list(s.split(' '))
a = list()
try:
    for i in range(len(s)):
        int(s[i])
except: print("Проверьте правильность ввода данных")
else:
    for i in range(len(s)):
        a.append(s[i])
        for j in range(0, i):
            a.append(s[j])
    for i in range(len(a)):
        print(a[i], end = ' ')