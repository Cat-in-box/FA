# -*- coding: utf-8 -*-
import math
print('Введите число х')
x=float(input())
if ((x**2-x**4)!=0) and ((3-x)>=0) and (abs((3-x)**(1/4))<=1):
    y=(((x+math.sin(x))**(1/3))/(x**2-x**4))*((math.asin((3-x)**(1/4)))**2)
    print(y)
else: print('Введённый х не входит в одз')