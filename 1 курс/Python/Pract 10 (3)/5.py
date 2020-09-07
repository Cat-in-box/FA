# -*- coding: utf-8 -*-
def R(n):
    if n > 0:
        print(n%10, end = ' ')
        R(n//10)
    
R(int(input('Ввод числа: ')))