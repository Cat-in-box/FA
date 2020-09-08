# -*- coding: utf-8 -*-
import copy
import random
import array as ar
import numpy as num

ar1 = ar.array ('i', [5, -7, 3, 8, -9, 10, 4, 2, -10, -8])
num1 = num.array ([[1,2,3,4,5], [2,5,7,3,1], [1,8,7,4,3]])

#1
s = 0
for i in ar1:
    if i>0 and i%2==0:
        s+=i
print('№1', s)

#2
s = 0
for i in range (len(ar1)):
    if i%2==0 and ar1[i]>s:
        s = ar1[i]
print('№2', s)

#3
h = 3
print('№3', end =' ')
for m in range(len(num1[0])):
    flag = False
    for n in range(len(num1)):
         if num1[n][m] == h:
             flag = True
    if flag:
        print(m+1, end =' ')
print('')

#4
s = 0
print('№4', end =' ')
for i in ar1:
    s+=i
s = s/len(ar1)
for i in ar1:
    if i<s:
        print(i, end = ' ')
print('')

#5
print('№5', min(ar1), end = ' ')
ar2 = copy.copy(ar1)
ar2.pop(ar2.index(min(ar1)))
print(min(ar2))

#6
a = -5
b = 5
ar2 = copy.copy(ar1)
i = 0
while i < len(ar2):
    if (a<=ar2[i]) and (ar2[i]<=b) and (ar2[i]!=0):
        ar2.pop(i)
        ar2.append(0)
    else:
        i+=1
print('№6 [' + str(a) + ', ' + str(b) + ']', ar2)

#7
s = 0
flag = False
for i in ar1:
    if flag:
        s+=abs(i)
    if i < 0:
        flag = True
print('№7', s)

#8
print('№8')
s = 0
numS = num.array([])
print('Введите названия книг или "конец", если список закончился')
while s != 'конец' and s != 'Конец':
    s = input()
    if s != 'конец' and s != 'Конец':
        numS = num.append(s, numS)
numS = num.append(input('Ведите новую книгу: '), numS)
print(sorted(numS))

#9
print('№9')
print(ar1)
#a
ar2 = copy.copy(ar1)
ar3 = ar.array ('i', [])
for i in ar2:
    if i>0:
        ar3.append(i)
ar3 = sorted(ar3)
s = 0
for i in range(len(ar2)):
    if ar2[i]>0:
        ar2[i] = ar3[s]
        s+=1
print('a)', ar2)
#b
ar2 = copy.copy(ar1)
ar3 = ar.array ('i', [])
for i in range(len(ar2)):
    if i%2==0:
        ar3.append(ar2[i])
ar3 = sorted(ar3)
s = 0
for i in range(len(ar2)):
    if i%2==0:
        ar2[i] = ar3[s]
        s+=1
print('b)', ar2)

#10
ar2 = ar.array ('i', [5, -7, 3, 10, 8, -9, 10, 4, 2, -10, -8, -7, 3, 4])
set1 = set(ar1)
set2 = set(ar2)
if set1 == set2:
    print('№10 Совпадают')
else:
    print('№10 Не совпадают')

#11
ar3 = ar.array ('i', [])
for i in range(len(ar1)):
    ar3.append(ar1[i])
    ar3.extend(ar1[:i])
print('№11', ar1)
print(ar3)

#12
ar2 = ar.array ('u', 'itmathrepetitorcatitmathrepetitmathrepetitor')
ar3 = ar.array ('u', 'itmathrepetitor')
print('№12', ar2)
for i in range(len(ar2)):
    if ar2[i:i+15] == ar3:
        ar2[i:i+15] = ar.array ('u', 'silence')
print(ar2)

#13*-16* в отдельных файлах из-за объемности кода

#17
print('№17')
ar2 = copy.copy(ar1)
k = int(input('Введите количество шагов: '))
n = input('Введите направление сдвига: ')
if n == 'вправо' or n == 'Вправо':
    print(ar2)
    for j in range(0, k, 1):
        a = 0
        for i in range(0, len(ar2)):
            b = ar2[i]
            ar2[i] = a
            a = b
        print(ar2)
elif n == 'влево' or n == 'Влево':
    print(ar2)
    for j in range(0, k):
        a = 0
        for i in range(len(ar2)-1, -1, -1):
            b = ar2[i]
            ar2[i] = a
            a = b
        print(ar2)
else:
    print('Такой сдвиг сделать не можем')

#18
ar2 = ar.array ('i', [])
for i in range (10):
    ar2.append(random.randint(-10, 10))
print('№18', ar2)
i=0
while i < len(ar2):
    if ar2[i]<0:
        ar2.pop(i)
    else:
        i+=1
print(ar2)

#19
ar2 = ar.array ('i', [])
s = input('№19\nВведите численный массив через ", ": ').split(', ')
for i in range (len(s)):
    s[i] = int(s[i])
ar2.extend(s)
print(ar2)
n = int(input('Введите новый элемент: '))
s = int(input('Введите его позицию в списке: '))-1
ar2.insert(s, n)
print(ar2)

#20
ar2 = ar.array ('i', [])
for i in range (10):
    ar2.append(random.randint(-10, 10))
ar3 = ar.array ('i', [])
s = input('№20\nВведите численный массив через ", ": ').split(', ')
for i in range (len(s)):
    s[i] = int(s[i])
ar3.extend(s)
if len(ar2) <= len(ar3):
    s = len(ar2)
else:
    s = len(ar3)
ar4 = ar.array ('i', [])
for i in range(s):
    ar4.append(ar2[i]+ar3[i])
print (ar2, '\n', ar3, '\n', ar4)

#21
ar2 = num.array([random.randint(-5, 4) for i in range(2000)])
pos = 0
neg = 0
zero = 0
for i in ar2:
    if i > 0:
        pos+=1
    elif i < 0:
        neg+=1
    else:
        zero+=1
print('№21')
num.set_printoptions(edgeitems=4)
print(ar2)
print('Положительных чисел:', pos, '\nОтрицательных чисел:', neg, '\nНулей:', zero)