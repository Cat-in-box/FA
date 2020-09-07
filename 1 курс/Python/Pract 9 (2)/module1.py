import math

class Figura():
	def Perimter(self):
		pass
	def Area(self):
		pass
	def Info(self):
		pass
		
class Rectangle(Figura):
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def Perimeter(self):
		return ((self.a+self.b)*2)
	def Area(self):
		return (self.a*self.b)
	def Info(self):
		print('Прямоугольник\na =', self.a, '\nb =', self.b, '\nПлощадь:', self.Area(), '\nПериметр:', self.Perimeter(), '\n')
		
class Circle(Figura):
	def __init__(self, r):
		self.r = r
	def Perimeter(self):
		return (2*math.pi*self.r)
	def Area(self):
		return (math.pi*self.r)
	def Info(self):
		print('Круг\nr =', self.r, '\nПлощадь:', self.Area(), '\nПериметр:', self.Perimeter(), '\n')
	
class Triangle(Figura):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	def Perimeter(self):
		return (self.a+self.b+self.c)
	def Area(self):
		return (math.sqrt((self.Perimeter()/2)*(self.Perimeter()/2-self.a)*(self.Perimeter()/2-self.b)*(self.Perimeter()/2-self.c)))
	def Info(self):
		print('Треугольник\na =', self.a, '\nb =', self.b, '\nc =', self.c, '\nПлощадь:', self.Area(), '\nПериметр:', self.Perimeter(), '\n')
		