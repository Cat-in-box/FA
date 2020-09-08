# -*- coding: utf-8 -*-
def R(n):
    global inp
    if n < inp:
        R(n*2)
    elif n == inp:
        print ('YES')
    else:
        print('NO')
    
inp = int(input('Ввод числа: '))
R(1)