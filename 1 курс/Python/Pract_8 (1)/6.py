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
		
if __name__ == '__main__':
	fake = Faker(['ru_RU'])
	item1 = Toy('Мишка', 800, 'Aurora', 'трикотаж, поролон', 2)
	item2 = Toy('Lego Friends', 1000, 'Lego', 'пластмасса', 5)
	item3 = Book('Стихи для детей', 'Агния Барто', 180, 'Эксмо', 3)
	item4 = Book('Хорошо быть тихоней', 'Стивен Чбоски', 315, 'Азбука', 18)
	item5 = Sport_equipment('Горные лыжи', 1500, 'Атомик', 10)
	item6 = Sport_equipment('Гантели', 190, 'York fitness', 15)
	
	lst = [item1, item2, item3, item4, item5, item6]
	for i in range(len(lst)):
		lst[i].Info()
	age = int(input('Введите возраст: '))
	print('Вы можете позволить себе следующие товары:\n')
	for i in range (len(lst)):
		if lst[i].Purchase(age):
			lst[i].Info()