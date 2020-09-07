# -*- coding: utf-8 -*-
def string_bin(x):
    global a, b
    while len(x)<(a+b):
        x = '0' + x
    return x

def R(n):
    global a, b, counter

    if n < (2**(a+b)):
        s = str(bin(n))
        s = string_bin(s[2:len(s)])
        
        if s.count('0')==a and s.count('1')==b:
            flag = True
            for i in range (len(s)-1):
                if s[i]=='0' and s[i+1]=='0':
                    flag = False
            if flag:
                counter+=1
        R(n+1)

a = int(input('Введите количество нулей: '))
b = int(input('Введите количество единиц:: '))

counter = 0

start = '01'
while len(start)<(a+b):
    start+='0'
start = int(start, 2)

R(start)
print (counter)