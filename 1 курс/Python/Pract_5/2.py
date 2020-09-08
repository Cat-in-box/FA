# -*- coding: utf-8 -*-
import os

def Sozdanie():
    global f
    f = open(input('Введите ПОЛНОЕ имя файла'), 'w')
    print('Пишите')
    f.write(input())
    f.close()
    
def Zapis():
    global f
    f = open(input('Введите ПОЛНОЕ имя файла'), 'a')
    print('Пишите')
    f.write(input())
    f.close()
    
def Chtenie():
    global f
    f = open(input('Введите ПОЛНОЕ имя файла'), 'r')
    f.read()
    f.close()
    
def Udalenie():
    f = input('Введите ПОЛНОЕ имя файла')
    if os.path.isfile(f):
        os.remove(f)
    else:
        print('Такого файла не существует')

def PUSK():
    inp = input('1. Создание нового файла\n2. Запись в файл\n3. Чтение файла\n4. Удаление файла\n5. Выход\n')
    if inp=='1':
        Sozdanie()
        PUSK()
    elif inp=='2':
        Zapis()
        PUSK()
    elif inp=='3':
        Chtenie()
        PUSK()
    elif inp=='4':
        Udalenie()
        PUSK()
    elif inp=='5':
        None
    else:
        print('Неизвестная команда')
        PUSK()
PUSK()