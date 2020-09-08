# -*- coding: utf-8 -*-
s = input('Введите список через пробел ')
s = list(s.split(' '))
a = list()
b = list()
try:
    for i in range(len(s)):
        int(s[i])
except: print("Проверьте правильность ввода данных")
else:
    for i in range(0, len(s), 2):
        if int(s[i])<0:
            a.append(s[i])
        if int(s[i])>=0:
            b.append(s[i])
    a.sort()
    b.sort()
    a.reverse()
    a=a+b
    j=0
    for i in range(len(s)):
        if i%2==0:
            s[i]=a[j]
            j+=1
        print(s[i], end=" ")