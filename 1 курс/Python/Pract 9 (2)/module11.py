from faker import Faker
import random

class Toy():
	def Info(self):
		pass
	def Check(self, color):
		if self.color == color:
			return True
		else:
			return False

class Cube(Toy):
	def __init__(self, color, price, material, a):
		self.color = color
		self.price = price
		self.material = material
		self.a = a
	def Info(self):
		print('Кубик\nЦвет:', self.color, '\nЦена:', self.price, '\nМатериал:', self.material, '\nРазмер ребра:', self.a, '\n')
	
class Ball(Toy):
	def __init__(self, color, price, material, d):
		self.color = color
		self.price = price
		self.material = material
		self.d = d
	def Info(self):
		print('Мяч\nЦвет:', self.color, '\nЦена', self.price, '\nМатериал:', self.material, '\nДиаметр:', self.d, '\n')

class Car(Toy):
	def __init__(self, name, color, price, manufacturer):
		self.name = name
		self.color = color
		self.price = price
		self.manufacturer = manufacturer
	def Info(self):
		print('Машинка\nНазвание:', self.name, '\nЦвет:', self.color, '\nЦена:', self.price, '\nПроизводитель:', self.manufacturer, '\n')
