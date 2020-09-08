# -*- coding: utf-8 -*-

def R(n, ost):
    if n>0:
        return R(n//10, ost*10+n%10)
    else:
        return ost

inp = int(input('Введите число: '))
print(R(inp, 0))