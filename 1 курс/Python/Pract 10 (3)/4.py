# -*- coding: utf-8 -*-
def R(n):
    if (len(n) == 1) or (len(n) == 0):
        print('YES')
    elif n[0] == n[len(n)-1]:
        R(n[1:len(n)-1])
    else:
        print('NO')
    
R(input('Ввод слова: '))
