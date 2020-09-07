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

if __name__ == '__main__':
	fake = Faker(['en_GB'])
	
	Person1 = Cube(fake.color_name(), random.randint(50, 500), 'пластмасса', random.randint(2, 20))
	Person2 = Ball(fake.color_name(), random.randint(50, 1500), 'полимер', random.randint(20, 1000))
	Person3 = Car(fake.name(), fake.color_name(), fake.random_int(300, 5000), fake.company())
	
	lst = [Person1, Person2, Person3]
	for i in range(len(lst)):
		lst[i].Info()

	inp = input('Введите цвет: ')
	print('По ашему запросу нашлось:\n')
	for i in range(len(lst)):
		if lst[i].Check(inp):
			lst[i].Info()
