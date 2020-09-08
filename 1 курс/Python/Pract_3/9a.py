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
        if int(s[i])>0:
            a.append(s[i])
    a.sort()
    j=0
    for i in range(len(s)):
        if int(s[i])>0:
            s[i]=a[j]
            j+=1
        print(s[i], end=" ")