s = input('Ведите числа через пробел ')
s = list(s.split(' '))
try:
    for i in range(len(s)):
        x=int(s[i])
except: print('Проверьте правильность ввода данных')
else:
    if len(s)>1:
        for i in range(len(s)-1):
            print(int(s[i-1])+int(s[i+1]), end = " ")
        print(int(s[len(s)-2])+int(s[0]))
    else: print(s[0])