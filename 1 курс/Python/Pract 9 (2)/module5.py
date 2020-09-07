from faker import Faker
import random

class Item():
	def Info(self):
		pass
	def Purchase(self, money):
		if self.price > money:
			return False
		else:
			return True

class Product(Item):
	def __init__(self, name, price, date_of_manufacture, shelf_life):
		self.name = name
		self.price = price
		self.date_of_manufacture = date_of_manufacture
		self.shelf_life = shelf_life
	def Info(self):
		print('Продукт\nНазвание:', self.name, '\nЦена:', self.price, '\nДата производства:', self.date_of_manufacture, '\nСрок годности:', self.shelf_life, '\n')
		
class Consignment(Item):
	def __init__(self, name, price, number_of_item, date_of_manufacture, shelf_life):
		self.name = name
		self.price = price
		self.number_of_item = number_of_item
		self.date_of_manufacture = date_of_manufacture
		self.shelf_life = shelf_life
	def Info(self):
		print('Партия\nНазвание:', self.name, '\nЦена за штуку:', self.price, '\nКоличество штук', self.number_of_item, '\nДата производства:', self.date_of_manufacture, '\nСрок годности:', self.shelf_life, '\n')
		
class Phone(Item):
	def __init__(self, name, price):
		self.name = name
		self.price = price
	def Info(self):
		print('Телефон\nНазвание:', self.name, '\nЦена:', self.price, '\n')
		