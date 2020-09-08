# -*- coding: utf-8 -*-
import datetime
d = {5238: ('Архангельск', 'Санкт-Петербург', datetime.time(14, 54), datetime.timedelta(hours=22, minutes=26), 0, 'Ладожский вокзал'), #Время отправления, время в пути
     3852: ('Санкт-Петербург', 'Архангельск', datetime.time(15, 10), datetime.timedelta(hours=22, minutes=26), 'Ладожский вокзал', 0),
     
     3877: ('Санкт-Петербург', 'Москва', datetime.time(21, 0), datetime.timedelta(hours=3, minutes=35), 'Московский вокзал', 'Ленинградский вокзал'),
     7738: ('Москва', 'Санкт-Петербург', datetime.time(19, 0), datetime.timedelta(hours=3, minutes=35), 'Ленинградский вокзал', 'Московский вокзал'),
     
     3677: ('Калининград', 'Москва', datetime.time(13, 3), datetime.timedelta(hours=19, minutes=6), 0 , 'Белорусский вокзал'),
     7736: ('Москва', 'Калининград', datetime.time(14, 3), datetime.timedelta(hours=19, minutes=6), 'Белорусский вокзал', 0),
     
     7711: ('Москва', 'Киров', datetime.time(13, 46), datetime.timedelta(hours=16, minutes=12), 'Ярославский вокзал', 0),
     1177: ('Киров', 'Москва', datetime.time(17, 43), datetime.timedelta(hours=16, minutes=12), 0, 'Ярославский вокзал'),
     
     1149: ('Киров', 'Екатеринбург', datetime.time(14, 50), datetime.timedelta(hours=12, minutes=44)),
     4911: ('Екатеринбург', 'Киров', datetime.time(16, 40), datetime.timedelta(hours=12, minutes=44)),
     
     7760: ('Москва', 'Казань', datetime.time(13, 0), datetime.timedelta(hours=14, minutes=48), 'Казанский вокзал', 0),
     6077: ('Казань', 'Москва', datetime.time(15, 17), datetime.timedelta(hours=14, minutes=48), 0, 'Казанский вокзал'),
     
     6049: ('Казань', 'Екатеринбург', datetime.time(2, 13), datetime.timedelta(hours=13, minutes=46)),
     4960: ('Екатеринбург', 'Казань', datetime.time(4, 54), datetime.timedelta(hours=13, minutes=46)),
     
     4920: ('Екатеринбург', 'Тюмень', datetime.time(18, 40), datetime.timedelta(hours=5, minutes=37)),
     2049: ('Тюмень', 'Екатеринбург', datetime.time(20, 40), datetime.timedelta(hours=5, minutes=37)),
     
     2017: ('Тюмень', 'Омск', datetime.time(9, 59), datetime.timedelta(hours=8, minutes=16)),
     1720: ('Омск', 'Тюмень', datetime.time(11, 59), datetime.timedelta(hours=8, minutes=16)),
     
     7754: ('Москва', 'Волгоград', datetime.time(4, 53), datetime.timedelta(hours=24, minutes=5), 'Павелецский вокзал', 0),
     5477: ('Волгоград', 'Москва', datetime.time(2, 47), datetime.timedelta(hours=24, minutes=5), 0, 'Павелецкий вокзал'),
     
     5473: ('Волгоград', 'Астрахань', datetime.time(17, 27), datetime.timedelta(hours=5, minutes=33)),
     7354: ('Астрахань', 'Волгоград', datetime.time(16, 33), datetime.timedelta(hours=5, minutes=33)),
     
     5435: ('Волгоград', 'Краснодар', datetime.time(0, 45), datetime.timedelta(hours=12, minutes=41)),
     3554: ('Краснодар', 'Волгоград', datetime.time(1, 26), datetime.timedelta(hours=12, minutes=41))}

Towns = ('Москва', 'Санкт-Петербург')

a = input('Введите пункт отправления: ')
b = input('Введите пункт назначения: ')

TimeNow = datetime.datetime.now()
print(TimeNow)

lst = []
l = []

def Function():
    global N, M, k, f, lst, l
    for i in d.keys():
        if (d[i][0]==N) and not(d[i][1]==M) and (i not in l): #Если есть связь, это не обратный рейс и по рейсу еще не проезжали(не зацикливаемся)
            l.append(i)
            if d[i][1]==b:
                lst.append(l.copy()) #Нашли пункт назначения
            elif (len(l)-1)<4: #Если нет - ищем дальше
                N=d[i][1]
                M=d[i][0]
                Function()
            l.pop()
            try:
                N=d[l[len(l)-1]][1]
                M=d[l[len(l)-1]][0]
            except:
                N=a
                M=0

if a==b:
    print('Вы ввели один и тот же город')
else:
    for i in d.keys():
        if d[i][0]==a:
            f=True
    for i in d.keys():
        if (d[i][1]==b) and f:
            f*=True
    if f:
        N=a
        M=0
        Function()
    print (lst, f)
    if not f or (len(lst)<1):
        print('Авиаперелеты между городами невозможны или требуется более 4х пересадок')
    else:
        TimeFast=datetime.timedelta(365)
        for i in range (len(lst)):
            f=False
            Time=TimeNow
            print('Маршрут №', i+1)
            for j in range (len(lst[i])):
                if (Time.hour<d[lst[i][j]][2].hour) or ((Time.hour==d[lst[i][j]][2].hour) and (Time.minute<d[lst[i][j]][2].minute)):
                    Time=datetime.datetime(Time.year, Time.month, Time.day, d[lst[i][j]][2].hour, d[lst[i][j]][2].minute)
                else:
                    Time=datetime.datetime(Time.year, Time.month, Time.day+1, d[lst[i][j]][2].hour, d[lst[i][j]][2].minute)
                if f:
                    if (d[lst[i][j]][0] in Towns) and d[lst[i][j]][4]!=d[lst[i][N]][5]:
                        Time = Time + datetime.timedelta(minutes=30)
                        print('    Требуется 30мин. на пересадку', d[lst[i][N]][5], '->', d[lst[i][j]][4])
                    print('    ----------------')
                print('    Рейс №', lst[i][j])
                print('   ', d[lst[i][j]][0], Time.strftime('%d/%m/%Y %H:%M'), '->', d[lst[i][j]][1], datetime.datetime.strftime((Time + d[lst[i][j]][3]), '%d/%m/%Y %H:%M'))
                Time = Time + d[lst[i][j]][3]
                f=True
                N=j
            print('    ----------------')
            print('    Приедете через: ', Time - TimeNow)
            if (Time - TimeNow)<TimeFast:
                TimeFast = Time - TimeNow
                k=i
        if len(lst)>1:
            print('Самый быстрый маршрут №', k+1)