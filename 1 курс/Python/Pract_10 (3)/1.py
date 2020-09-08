# -*- coding: utf-8 -*-
def R(n):
    global inp
    print (n, end = ' ')
    if n < inp:
        R(n+1)
    
inp = int(input('Ввод числа: '))
R(1)