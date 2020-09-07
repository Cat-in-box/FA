from faker import Faker
import random

class Transport():
	def Info(self):
		pass
	def Check(self, x, y, z):
		if (abs(self.x) <= abs(x)) and (abs(self.y) <= abs(y)) and (abs(self.z) <= abs(z)):
			return True
		else:
			return False

class Plane(Transport):
	def __init__(self, name, max_speed, max_hight, count, x, y, z):
		self.name = name
		self.max_speed = max_speed
		self.max_hight = max_hight
		self.count = count
		self.x = x
		self.y = y
		self.z = z
	def Info(self):
		print('Самолет\nМарка:', self.name, '\nМаксимальная скорость:', self.max_speed, '\nМаксимальная высота:', self.max_hight, '\nКоличество пассажиров', self.count, '\nКоординаты:', self.x, self.y, self.z, '\n')
	
class Car(Transport):
	def __init__(self, name, number, year, x, y, z):
		self.name = name
		self.number = number
		self.year = year
		self.x = x
		self.y = y
		self.z = z
	def Info(self):
		print('Автомобиль\nМарка:', self.name, '\nНомер:', self.number, '\nГод выпуска:', self.year, '\nКоординаты:', self.x, self.y, self.z, '\n')

class Ship(Transport):
	def __init__(self, name, speed, count, notes, x, y, z):
		self.name = name
		self.speed = speed
		self.count = count
		self.notes = notes
		self.x = x
		self.y = y
		self.z = z
	def Info(self):
		print('Корабль\nНазвание:', self.name, '\nСкорость:', self.speed, '\nКоличество пассажиров:', self.count, '\nПорт приписки:', self.notes, '\nКоординаты:', self.x, self.y, self.z, '\n')

if __name__ == '__main__':
	fake = Faker(['en_GB'])
	
	Person1 = Plane(fake.name(), random.randint(800, 1000), random.randint(8000, 11000), random.randint(40, 850), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000))
	Person2 = Car(fake.company(), 'P425BP77', fake.year(), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000))
	Person3 = Ship(fake.name(), random.randint(40, 120), fake.random_int(500, 5000), fake.bs(), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000))
	
	lst = [Person1, Person2, Person3]
	for i in range(len(lst)):
		lst[i].Info()
	print('Введите координаты')
	inp_x = int(input('x -> '))
	inp_y = int(input('y -> '))
	inp_z = int(input('z -> '))
	print('\nОтносительно 0, 0, 0 в пределах заданных координат находятся сделующие транспортные средства:\n')
	for i in range(len(lst)):
		if lst[i].Check(inp_x, inp_y, inp_z):
			lst[i].Info()
