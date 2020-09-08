def Hash(s, m):
    summa = 0
    for symb in s:
        summa = ord(symb) % m + 13
    return summa

inp = input('Что хешируем? ')
m = input('Параметр для хеширования: ')
if m == '' or m == '0':
    s = Hash(inp, 47)
else:
    s = Hash(inp, int(m))
print(s)