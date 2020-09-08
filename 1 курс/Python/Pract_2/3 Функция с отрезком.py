# -*- coding: utf-8 -*-
import math
print('Введите начало промежутка')
l=float(input()) #в задании 2
print('Введите конец промежутка')
r=float(input()) #в задании 3
print('Введите число значений n')
n=float(input()) #в задании 10
t=(r-l)/n
while l<r:
    print('x=', l)
    if ((l**2-l**4)!=0) and ((3-l)>=0) and (abs((3-l)**(1/4))<=1):
        y=(((l+math.sin(l))**(1/3))/(l**2-l**4))*((math.asin((3-l)**(1/4)))**2)
        print('y=', y)
    else: print('Введённый х не входит в одз')
    l+=t