import numpy as np

inp = input('Введите размер первой матрицы в виде M*N: ')
M = int(inp[0:inp.find('*')])
N = int(inp[inp.find('*')+1:])

inp = input('Введите элементы матрицы через ", ": ').split(', ')
for i in range(len(inp)):
    inp[i] = int(inp[i])
a = np.matrix(inp)
a = a.reshape(M, N)

op = input('Выберите действие: +, -, *: ')

inp = input('Введите размер второй матрицы в виде M*N: ')
M = int(inp[0:inp.find('*')])
N = int(inp[inp.find('*')+1:])

inp = input('Введите элементы матрицы через ", ": ').split(', ')
for i in range(len(inp)):
    inp[i] = int(inp[i])
b = np.matrix(inp)
b = b.reshape(M, N)

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
else:
    print('Неизвестная операция')