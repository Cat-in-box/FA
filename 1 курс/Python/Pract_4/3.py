# Возьмите подходящие данные из задания 1 или 2

d = {}
for i in range (len(fio)):
    d[ad[i]] = fio[i]
print(d)
a = int(input('Введите страну/номер: '))
if d.get(a)==None:
    if input('Такой записи нет. СОздать новую запись?')=='Да':
        d[a] = input('Введите новое имя: ')
        print('Создана новая запись')
else: print(d.get(a))
print(d)