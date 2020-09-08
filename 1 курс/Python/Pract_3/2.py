# -*- coding: utf-8 -*-
s = input('Введите числа через пробел ')
s = list(s.split(' '))
try:
    for i in range(len(s)):
        x=int(s[i])
except: print("Проверьте правильность ввода данных")
else:
    s1 = []
    for i in range(len(s)):
        if (s.count(s[i]))>1 and s[i] not in s1:
            s1.append(s[i])
    for i in range(len(s1)):
        print(s1[i], end = " ")
    if len(s1)==0:
        print("Повторений нет")