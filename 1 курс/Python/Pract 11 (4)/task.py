# -*- coding: utf-8 -*-
import texttable
from datetime import datetime

class main():
    def __init__(self):
        self.Group_list = []
    
    def start(self):
        flag = True
        inp = input('Выберите группу: ')
        for l in self.Group_list:
            if l.id == inp:
                flag = False
                l.working()
        if flag:
            inp = input('Такой группы еще нет, хотите создать? ')
            if inp.upper() == 'ДА':
                self.group_create()

    def group_create(self):
        Group_obj = Group(input('Введите новую группу: '))
        self.Group_list.append(Group_obj)
        Group_obj.working()

class Group():
    def __init__(self, id):
        self.id = id
        self.students = []
        self.table = texttable.Texttable()

        self.table.add_rows([['Фамилия', 'Имя', 'Практика 1', 'Практика 2', 'Практика 3', 'Тест 1', 'Тест 2', 'Тест 3', 'Контрольная работа', 'Промежуточная аттестация', 
        'Практика 4', 'Практика 5', 'Практика 6', 'Практика 7', 'Тест 4', 'Тест 5', 'Тест 6', 'Тест 7', 'Работа в семестре', 'Экзамен', 'Итоговая']])
    
    def print_table(self):
        for st in self.students:
            a = [st.surname, st.name, st.practics[0].mark, st.practics[1].mark, st.practics[2].mark, st.tests[0], st.tests[1], st.tests[2], st.check, 
            st.practics[0].mark + st.practics[1].mark + st.practics[2].mark + st.tests[0] + st.tests[1] + st.tests[2] + st.check,
            st.practics[3].mark, st.practics[4].mark, st.practics[5].mark, st.practics[6].mark, st.tests[3], st.tests[4], st.tests[5], st.tests[6],
            st.practics[3].mark + st.practics[4].mark + st.practics[5].mark + st.practics[6].mark + st.tests[3] + st.tests[4] + st.tests[5] + st.tests[6],
            st.exam]
            i = a[9]+a[18]+a[19]
            if i < 51:
                a.append(str(i)+'(2)')
            elif 50 < i < 71:
                a.append(str(i)+'(3)')
            elif 70 < i < 87:
                a.append(str(i)+'(4)')
            elif i > 85:
                a.append(str(i)+'(5)')
            self.table.add_rows([a])
        print (self.table.draw())
    
    def working(self):
        inp = input('Выберите действие:\n1.Работа со студентом\n2.Вывод информации по группе\n3.Выход')
        if inp != '3':
            if inp == '1':
                flag = True
                inp = input('Введите фамилию и имя студента: ')
                for s in self.students:
                    if s.surname == inp[0:inp.find(' ')] and s.name == inp[inp.find(' ')+1:]:
                        flag = False
                        s.working()
                if flag:
                    inp = input('Такого студента еще нет, хотите добавить? ')
                    if inp.upper() == 'ДА':
                        self.student_create()
            elif inp == '2':
                self.print_table()
            self.working()
    
    def student_create(self):
        Student_obj = Student(input('Введите новую фамилию: '), input('Введите новое имя: '))
        self.students.append(Student_obj)
        self.students = sorted(key=lambda x: x.surname)
        Student_obj.working()

class Student():
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
        self.practics = [Task(), Task(), Task(), Task(), Task(), Task(), Task()]
        self.check = 0
        self.tests = [0, 0, 0, 0, 0, 0, 0]
        self.exam = 0

    def working(self):
        inp = input('Выберите действие:\n1.Работа с практикой\n2.Изменить результат контрольной работы\n3.Работа с тестами\n4.Экзамен\n5.Выход')
        if inp != '5':
            if inp == '1':
                self.pract_work()
            elif inp == '2':
                self.check_work()
            elif inp == '3':
                self.tests_work()
            elif inp == '4':
                self.exam_work()
            self.working()
    
    def pract_work(self):
        try:
            inp = int(input('Введите номер практики от 1 до 7: '))
        except:
            print('Такой практики нет')
            self.pract_work()
        else:
            if inp in range(1, 8):
                self.practics[inp-1].working()
            else:
                print('Такой практики нет')
                self.pract_work()

    def check_work(self):
        try:
            inp = int(input('Введите оценку за контрольную от 0 до 5: '))
        except:
            print('Неправильный ввод')
            self.check_work()
        else:
            if inp in range(0, 6):
                self.check = inp
            else:
                print('Неправильный ввод')
                self.check_work()
    
    def _marking(self, a):
        try:
            inp = int(input('Введите оценку за тест от 0 до 2: '))
        except:
            print('Неправильный ввод')
            self._marking(a)
        else:
            if inp in range(0, 3):
                self.practics[a] = inp
            else:
                print('Неправильный ввод')
                self._marking(a)

    def tests_work(self):
        try:
            inp = int(input('Введите номер теста от 1 до 7: '))
        except:
            print('Такого теста нет')
            self.tests_work()
        else:
            if inp in range(1, 8):
                self._marking(inp-1)
            else:
                print('Такого теста нет')
                self.tests_work()
    
    def exam_work(self):
        try:
            inp = int(input('Введите баллы за экзамен от 0 до 60: '))
        except:
            print('Неправильный ввод')
            self.exam_work()
        else:
            if inp in range(0, 61):
                self.exam = inp
            else:
                print('Неправильный ввод')
                self.exam_work()

class Task():
    def __int__(self):
        self.a = None
        self.b = None
        self.mark = 0
    
    def working(self):
        try:
            inp = input('Введите дату выполения в виде "01.01.2001" или ничего:')
            if inp != '':
                inp = datetime.strptime(inp, '%d.%m.%Y')
                self.a = inp
                inp = input('Введите дату защиты в виде "01.01.2001" или ничего:')
                if inp != '':
                    inp = datetime.strptime(inp, '%d.%m.%Y')
                    self.b = inp
                    self.mark = 3
        except:
            print('Вы ошиблись при вводе дат, повторите попытку')
            self.working()
        
if __name__ == '__main__':
    main_obj = main()
    main_obj.start()