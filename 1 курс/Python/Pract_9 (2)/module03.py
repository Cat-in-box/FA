import random

class  Posledovatelnost():
	def __init__(self):
		self.spisok = []
	def Adding(self):
		self.spisok.append(input('Введите последовательность через ,\n').split(','))
	def Random_adding(self):
		self.spisok.append([random.randint( -10, 10) for _ in range(10)])
        