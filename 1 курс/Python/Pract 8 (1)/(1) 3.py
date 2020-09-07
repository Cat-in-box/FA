import random

class  Posledovatelnost():
	def __init__(self):
		self.spisok = []
	def Adding(self):
		self.spisok.append(input('Введите последовательность через ,\n').split(','))
	def Random_adding(self):
		self.spisok.append([random.randint( -10, 10) for _ in range(10)])

spisok1 = Posledovatelnost()

def start():
	print(spisok1.spisok)
	a = input('Желаете создать вложенную последовательность?\n')
	if a == 'да' or a == 'Да':
		a = input('Заполнить ее автоматически?\n')
		if a == 'да' or a == 'Да':
			spisok1.Random_adding()
		elif a == 'нет' or a == 'Нет':
			spisok1.Adding()
		else:
			print('Неизвестная команда')
		start()
	elif a == 'нет' or a == 'Нет':
		pass
	else:
		print('Неизвестная команда')
		start()
		
start()