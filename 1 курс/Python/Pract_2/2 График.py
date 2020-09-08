print('Введите число R(радиус окружности)')
R = float(input())
print('Введите x')
x = float(input())
if abs(x)>R:
    print('y = 0')
elif x<0:
    print('y =', x+R)
elif x==0:
    print('y =', R)
elif x>0:
    y = (R**2 - x**2)**0.5 #т.к. r^2 = x^2 + y^2
    print('y =', y)