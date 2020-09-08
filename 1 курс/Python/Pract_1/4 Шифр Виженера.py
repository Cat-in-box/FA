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
        L = len(s)
        while len(k)<len(s):
            k = k+k
            k = k[0:L]
            if g == 1:
                for i in range(0, L):
                    n = A.find(s[i]) + A.find(k[i])
                    print(A[n%26], end="")
            if g == 0:
                for i in range(0, L):
                    n = A.find(s[i]) - A.find(k[i])
                    print(A[n], end="")
    else: print ('Ошибка во входных данных')
else: print ('Ошибка во входных данных')