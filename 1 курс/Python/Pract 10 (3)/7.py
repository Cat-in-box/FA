# -*- coding: utf-8 -*-

def R():
    n = int(input('Ввод числа: '))
    if n > 0:
        if n%2 == 1:
            print (n, '- нечетное')
        R()
        
R()