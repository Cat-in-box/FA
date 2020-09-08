# -*- coding: utf-8 -*-
A = ' 1234567890АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя!?.,:;-"()'
print ('Введите строку (кириллица, цифры, знаки)')
s = str(input())
print('Введите ключ')
k = int(input())
k %= 87
print('Если хотите зашифровать - введите 1, дешифровать - 0')
g = int(input())
L = len(s)
if g == 1:
    for i in range(0, L):
        n = A.find(s[i])
        print(A[n+k], end="")
if g == 0:
    for i in range(0, L):
        n = A.find(s[i])
        print(A[n-k], end="")