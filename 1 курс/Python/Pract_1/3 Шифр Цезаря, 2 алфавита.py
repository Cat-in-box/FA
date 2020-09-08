# -*- coding: utf-8 -*-
A = '1234567890abcdefghijklmnopqrstuvwxyz'
print ('Введите строку (латиница строчные, цифры)')
s = input()
if s.islower()==True:
    print('Введите ключ №1')
    k1 = int(input())
    k1 %= 36
    print('Введите ключ №2')
    k2 = int(input())
    k2 %= 36
    print('Если хотите зашифровать - введите 1, дешифровать - 0')
    g = int(input())
    L = len(s)
    if g == 1:
        for i in range(0, L):
            if (i%2==0):
                n = A.find(s[i])
                print(A[n+k1], end="")
            if (i%2==1):
                n = A.find(s[i])
                print(A[n+k2], end="")
    if g == 0:
        for i in range(0, L):
            if (i%2==0):
                n = A.find(s[i])
                print(A[n-k1], end="")
            if (i%2==1):
                n = A.find(s[i])
                print(A[n-k2], end="")
else: print ('Ошибка во входных данных')