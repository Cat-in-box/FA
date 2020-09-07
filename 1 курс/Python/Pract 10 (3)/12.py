# -*- coding: utf-8 -*-
def R1():
    n = int(input('Ввод числа: '))
    if n > 0:
        print(n)
        R2()

def R2():
    n = int(input('Ввод числа: '))
    if n > 0:
        R1()

R1()