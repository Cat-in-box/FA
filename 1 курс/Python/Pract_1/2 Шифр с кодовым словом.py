# -*- coding: utf-8 -*-
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print ('Введите строку (латиница ЗАГЛАВНЫЕ)')
s = str(input())
if s.isupper()==True:
    print('Введите кодовое слово (латиница ЗАГЛАВНЫЕ)')
    k = str(input())
    if k.isupper()==True:
        print('Если хотите зашифровать - введите 1, дешифровать - 0')
        g = int(input())
        L = len(k)
        B = A
        for i in range(0, L):
            B = B.replace(k[i],"")
        B = k + B
        L = len(s)
        if g == 1:
            for i in range(0, L):
                n = A.find(s[i])
                print(B[n], end="")
        if g == 0:
            for i in range(0, L):
                n = B.find(s[i])
                print(A[n], end="")
    else: print ('Ошибка во входных данных')
else: print ('Ошибка во входных данных')