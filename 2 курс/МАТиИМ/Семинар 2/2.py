# -*- coding: utf-8 -*-
import numpy as np
'''
l = float(input("Введите интенсивность поступления требований: "))
u = float(input("Введите интенсивность обслуживания требований одним каналом: "))

m = int(input("Введите количество каналов: "))
n = int(input("Введите количество мест в очереди: "))
'''
l = 3
u = 2
m = 5
n = 1

P = np.zeros((m+n+1, m+n+1))

for i in range (m+n):
    P[i, i+1] = l
    P[i+1, i] = u*(i+1)
print(P)

M = P
for i in range (m+n):
    M[i, i] = M[i].sum()
for i in range (m+n):
    for j in range (m+n):
        if i !=j:
            M[i, j], M[j, i] = M[j, i], M[i, j]
print(M)

M_ = M
for i in range (m+n+1):
    M_[m+n, i] = 1
print(M_)

B = [0, 0, 0, 0, 0, 0, 1]

X = np.linalg.inv(M_).dot(B)
print(X)