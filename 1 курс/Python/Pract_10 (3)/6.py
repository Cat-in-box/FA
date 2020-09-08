# -*- coding: utf-8 -*-
def R(n, k):
    if k == n or n == 1:
        print('YES')
    elif n%k == 0:
        print ('NO')
    elif k < n:
        R(n, k+1)
    
R(int(input('Ввод числа: ')), 2)