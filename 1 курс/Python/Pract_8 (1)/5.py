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
		
if __name__ == '__main__':
	fake = Faker(['ru_RU'])
	Item1 = Product(fake.word(), random.randint(100, 5000), fake.date(), str(random.randint(1, 24))+' месяцев')
	Item2 = Consignment(fake.word(), random.randint(100, 5000), random.randint(100, 1000), fake.date(), str(random.randint(1, 24))+' месяцев')
	Item3 = Phone(fake.word(), random.randint(500, 100000))
	Item4 = Phone(fake.word(), random.randint(500, 100000))
	
	lst = [Item1, Item2, Item3, Item4]
	for i in range(len(lst)):
		lst[i].Info()
	money = int(input('Введите максимальную сумму, на которую хотите сделать заказ: '))
	print('Вы можете позволить себе следующие товары:\n')
	for i in range (len(lst)):
		if lst[i].Purchase(money):
			lst[i].Info()