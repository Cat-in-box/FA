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
