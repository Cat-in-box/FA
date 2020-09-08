import math

class Telo():
	def Perimter(self):
		pass
	def Area(self):
		pass
	def Info(self):
		pass
		
class Parallelepiped(Telo):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	def Obem(self):
		return (self.a*self.b*self.c)
	def Area(self):
		return (self.a*self.b*2+self.a*self.c*2+self.b*self.c*2)
	def Info(self):
		print('Параллелепипед\na =', self.a, '\nb =', self.b, '\nc =', self.c, '\nПлощадь поверхности:', self.Area(), '\nОбъем:', self.Obem(), '\n')
		
class Shar(Telo):
	def __init__(self, r):
		self.r = r
	def Obem(self):
		return ((4*math.pi*(self.r**2))/3)
	def Area(self):
		return (4*math.pi*(self.r**2))
	def Info(self):
		print('Шар\nr =', self.r, '\nПлощадь поверхности:', self.Area(), '\nОбъем:', self.Obem(), '\n')
	
class Piramida(Telo):
	def __init__(self, a, b, c, h):
		self.a = a
		self.b = b
		self.c = c
		self.h = h
	def Obem(self):
		return ((self.a*self.b*self.h)/3)
	def Area(self):
		return (self.a*self.b + 2*math.sqrt(((self.a+2*self.c)/2)*((self.a+2*self.c)/2-self.a)*(((self.a+2*self.c)/2-self.c))**2) + 2*math.sqrt(((self.b+2*self.c)/2)*((self.b+2*self.c)/2-self.b)*(((self.b+2*self.c)/2-self.c)**2)))
	def Info(self):
		print('Пирамида\na =', self.a, '\nb =', self.b, '\nc =', self.c, '\nh =', self.h, '\nПлощадь поверхности:', self.Area(), '\nОбъем:', self.Obem(), '\n')
		