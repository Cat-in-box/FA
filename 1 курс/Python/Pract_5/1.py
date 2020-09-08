# -*- coding: utf-8 -*-
y = input('Введите квадратное уравнение в виде: выражение=0 ')

def F0():
    print('Уравнение не имеет решений')

def F1(a, b):
    x = -b/(2*a)
    print('x =', x)

def F2(a, b):
    x1 = (-b+(D**0.5))/(2*a)
    x2 = (-b-(D**0.5))/(2*a)
    print('x1 =', x1)
    print('x2 =', x2)

try:
    y = y.replace(' ', '')
    if int(y[y.find('=')+1:])!=0:
        print('Уравнение введено неверно')
    else:
        if y.find('x^2')==0:
            a = 1
        else:
            a = int(y[:y.find('x^2')])

        y = y[y.find('x^2')+3:y.find('=')]
        print('a =', a)
        if y.find('x')==-1:
            b = 0
        else:
            b = int(y[0:y.find('x')])
        y = y[y.find('x')+1:]
        print('b =', b)
        if len(y)>0:
            c = int(y[y.find('x')+1:])
        else:
            c = 0
        print('c =', c, '\n')
        D = (b**2)-(4*a*c)
        if D<0:
            F0()
        elif D==0:
            F1(a, b)
        else:
            F2(a, b)
except:
    print('Уравнение введено неверно')