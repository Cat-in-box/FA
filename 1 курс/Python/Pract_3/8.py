s = input('Введите список ')
s = list(s.split(', '))
a = s.copy
s.sort()
if s!=a:
    print('Список введен не в алфавитном порядке')
else:
    s.append(input('Введите новую книгу '))
    s.sort()
    print(s)