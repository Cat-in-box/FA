# -*- coding: utf-8 -*-
a = input("Введите список через пробел ")
a = list(a.split(" "))
k=0
for i in range(len(a)//2):
    if a[i]==a[len(a)-1-i]:
        k+=1
if k==(len(a)//2):
    print("Список симметричен")
else: print("Список не симметричен")