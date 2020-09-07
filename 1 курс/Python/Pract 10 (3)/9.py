# -*- coding: utf-8 -*-

def R():
    n = input('Ввод числа: ')
    if n != '00':
        r = R()
        if n == '1':
            return r+int(n)
        else:
            return r
    else:
        return 0

print(R())