# -*- coding: utf-8 -*-
import datetime

class obj():
    def __init__(self, person, value):
        self.person = person
        self.value = value

class Student():
    def __init__(self, surname, name, patronymic, birthdate, course, group, progr, math, hist, law, bank, go_next=None):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate
        self.course = course
        self.group = group
        self.progr = progr
        self.math = math
        self.hist = hist
        self.law = law
        self.bank = bank
        self.next = go_next
    def Sort(self):
        for i in range(1, 6):
            lst = []
            flag = False
            self = Student1
            while self:
                if self.course == i:
                    lst.append(self)
                    flag = True
                self = self.next
            if flag:
                print(i, 'курс')
                lst = sorted(lst, key=lambda x: x.surname)
                for i in lst:
                    print(i.surname, i.name, i.patronymic)
    def Medium(self):
        lst = []
        print('\nСредний балл групп по предметам')
        while self:
            if self.group not in lst:
                lst.append(self.group)
            self = self.next
        for i in lst:
            self = Student1
            progr = 0
            math = 0
            hist = 0
            law = 0
            bank = 0
            count = 0
            while self:
                if self.group == i:
                    progr += self.progr
                    math += self.math
                    hist += self.hist
                    law += self.law
                    bank += self.bank
                    count += 1
                self = self.next
            print(i, '\nПрограмированние:', progr/count, '\nМатематика:', math/count, '\nИстория:', hist/count, '\nПраво:', law/count, '\nБанковское дело:', bank/count)
    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today.month < self.birthdate.month:
            age -= 1
        elif today.month == self.birthdate.month and today.day < self.birthdate.day:
            age -= 1
        return age
    def MinMax(self):
        mn = obj(self, datetime.date(1900, 5, 4))
        mx = obj(self, datetime.date(2020, 5, 4))
        while self:
            if self.birthdate > mn.value:
                mn.value = self.birthdate
                mn.person = self
            elif self.birthdate < mx.value:
                mx.value = self.birthdate
                mx.person = self
            self = self.next
        print('\nСамый старший студент:', mx.person.surname, mx.person.name, mx.person.patronymic, mx.person.get_age(), 'лет')
        print('Самый младший студент:', mn.person.surname, mn.person.name, mn.person.patronymic, mn.person.get_age(), 'лет')
    def Best(self):
        lst = []
        print('\nЛучший по успеваемости студент в группе')
        while self:
            if self.group not in lst:
                lst.append(self.group)
            self = self.next
        for i in lst:
            self = Student1
            best = obj(self, 0)
            while self:
                if self.group == i and (self.progr + self.math + self.hist + self.law + self.bank)/5 > best.value:
                    best.person = self
                    best.value = (self.progr + self.math + self.hist + self.law + self.bank)/5
                self = self.next
            print(i, best.person.surname, best.person.name, best.person.patronymic, best.value)
        
Student1 = Student('Молчанов', 'Аристарх', 'Тихонович', datetime.date(1996, 4, 1), 1, 'ПИ-1', 5, 5, 3, 4, 3)
Student2 = Student('Савин', 'Аристарх', 'Владимирович', datetime.date(1996, 8, 23), 1, 'ПИ-2', 4, 3, 4, 3, 5)
Student3 = Student('Тетерин', 'Ермолай', 'Вадимович', datetime.date(1996, 9, 16), 2, 'ПИ-3', 3, 3, 5, 4, 5)
Student4 = Student('Ершов', 'Егор', 'Святославович', datetime.date(1997, 5, 27), 1, 'ПИ-4', 5, 3, 4, 4, 4)
Student5 = Student('Фадеев', 'Моисей', 'Германович', datetime.date(1997, 8, 5), 2, 'ПИ-3', 4, 4, 5, 3, 5)
Student6 = Student('Савельева', 'Маргарита', 'Протасьевна', datetime.date(1998, 8, 26), 2, 'ПИ-2', 5, 3, 4, 3, 4)
Student7 = Student('Романова', 'Тамара', 'Эдуардовна', datetime.date(2000, 2, 21), 2, 'ПИ-4', 5, 3, 3, 5, 5)
Student8 = Student('Крюкова', 'Агата', 'Всеволодовна', datetime.date(2000, 3, 25), 1, 'ПИ-3', 5, 4, 5, 4, 4)
Student9 = Student('Галкина', 'Евдокия', 'Геннадьевна', datetime.date(2001, 3, 11), 1, 'ПИ-2', 4, 5, 4, 3, 5)
Student10 = Student('Хохлова', 'Доминика', 'Лукьяновна', datetime.date(2001, 3, 19), 2, 'ПИ-1', 3, 3, 5, 4, 5)

Student1.next = Student2
Student2.next = Student3
Student3.next = Student4
Student4.next = Student5
Student5.next = Student6
Student6.next = Student7
Student7.next = Student8
Student8.next = Student9
Student9.next = Student10

Student1.Sort()
Student1.Medium()
Student1.MinMax()
Student1.Best()