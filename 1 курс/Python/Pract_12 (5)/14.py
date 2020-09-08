# -*- coding: utf-8 -*-
class Group:
    def __init__(self, number=None, members=None, go_previous=None, go_next=None):
        self.number = number
        self.members = members
        self.previous = go_previous
        self.next = go_next
    def __str__(self):
        return str(self.cargo)
    def Info(self):
        while self:
            print(self.number)
            self.members.Info()
            self = self.next
class Person:
    def __init__(self, name=None, go_next=None):
        self.name = name
        self.next = go_next
    def __str__(self):
        return str(self.cargo)
    def Info(self):
        while self:
            print(self.name)
            self = self.next
Group1 = Group()
Group2 = Group()
Group3 = Group()
Group4 = Group()
Group5 = Group()
Group1.next = Group2
Group2.next = Group3
Group3.next = Group4
Group4.next = Group5
Group2.previous = Group1
Group3.previous = Group2
Group4.previous = Group3
Group5.previous = Group4
Person1 = Person()
Person2 = Person()
Person3 = Person()
Person4 = Person()
Person5 = Person()
Person6 = Person()
Person7 = Person()
Person8 = Person()
Person9 = Person()
Person10 = Person()
Person1.next = Person2
Person3.next = Person4
Person5.next = Person6
Person7.next = Person8
Person9.next = Person10
Group1.members = Person1
Group2.members = Person3
Group3.members = Person5
Group4.members = Person7
Group5.members = Person9
print ('№14 Создан')