from faker import Faker
import random

class Item():
	def Info(self):
		pass
	def Purchase(self, money):
		if self.age > age:
			return False
		else:
			return True

class Toy(Item):
	def __init__(self, name, price, manufacturer, material, age):
		self.name = name
		self.price = price
		self.manufacturer = manufacturer
		self.material = material
		self.age = age
	def Info(self):
		print('Игрушка\nНазвание:', self.name, '\nЦена:', self.price, '\nПрозводитель:', self.manufacturer, '\nМатериал:', self.material, 'Возраст:', str(self.age)+'+', '\n')
		
class Book(Item):
	def __init__(self, name, author, price, publisher, age):
		self.name = name
		self.author =  author
		self.price = price
		self.publisher = publisher
		self.age = age
	def Info(self):
		print('Книга\nНазвание:', self.name, '\nАвтор:', self.author, '\nЦена', self.price, '\nИздательство:', self.publisher, '\nВозраст:', str(self.age)+'+', '\n')
		
class Sport_equipment(Item):
	def __init__(self, name, price, manufacturer, age):
		self.name = name
		self.price = price
		self.manufacturer = manufacturer
		self.age = age
	def Info(self):
		print('Спортинвентарь\nНазвание:', self.name, '\nЦена:', self.price, '\nПрозводитель:', self.manufacturer, 'Возраст:', str(self.age)+'+', '\n')
		