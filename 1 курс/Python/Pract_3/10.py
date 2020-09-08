# -*- coding: utf-8 -*-
s = input('Введите список через пробел ')
s = list(s.split(' '))
c = input('Введите список через пробел ')
c = list(c.split(' '))
try:
    for i in range(len(s)):
        int(s[i])
    for i in range(len(c)):
        int(c[i])
except: print("Проверьте правильность ввода данных")
else:
    s.sort()
    c.sort()
    if s==c:
        print('Множества списков совпадают')
    else:
        print('Множества списков не совпадают')