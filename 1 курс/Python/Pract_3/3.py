# -*- coding: utf-8 -*-
import numpy as np
N = int(input("Введите число строк "))
M = int(input("Введите число столбцов "))
a = np.random.randint(-100, 100, (N, M))
print(a)
lst = list()
H = int(input("Введите число H "))
for i in range(N):
    for j in range(M):
        if a[i][j]==H:
            lst.append(j+1)
lst = list(set(lst))
if len(lst)>0:
    print("Число H встечается в столбце(цах) ", end = "")
    for i in range(len(lst)):
        print(lst[i], end = " ")
else: print("Число H не встечается в матрице")