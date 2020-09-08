# -*- coding: utf-8 -*-
import pandas as pd
import datetime

class Group():
    def __init__(self, id, surname, name, practics, check, tests):
        self.id = id
        self.surname = surname
        self.name = name
        self.practics = [] #в формате [(номер, количество баллов), (), ...]
        self.check = check
        self.tests = tests #в формате [(номер, количество баллов), (), ...]

class Task():
    def __int__(self, ):
        self.start = datetime.datetime.strptime(input('Введите дату задания практической работы в формате DD.MM.YYYY: '),  '%d.%m.%Y')
        
    def app(self):
        if datatime.date.today() == self.start:
            print('topp')

file = 'example.xlsx'

xl = pd.ExcelFile(file)



writer = pd.ExcelWriter('Аттестация.xlsx', engine='xlsxwriter')
Data.to_excel(writer, 'Sheet1')
writer.save()
'''