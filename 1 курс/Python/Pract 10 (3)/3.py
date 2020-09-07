# -*- coding: utf-8 -*-
def R(n):
    global f
    f += n%10
    if n > 0:
        R(n//10)
    
f = 0
R(int(input('Ввод числа: ')))
print (f)