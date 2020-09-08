import math

class Triangle():
	def __init__(self, a, b, alfa):
		self.a = a
		self.b = b
		self.alfa = alfa
	def Area(self):
		return (self.a*self.b*math.sin(self.alfa))/2
	def Perimeter(self):
		return self.a+self.b+math.sqrt(self.a**2+self.b**2-2*self.a*self.b*math.cos(self.alfa))
	def Info(self):
		print('Треугольник', '\nПлощадь: ', self.Area(), '\nПериметр: ', self.Perimeter(), '\n')
		
class Pryamougolnyj(Triangle):
	def __init__(self, a, b, alfa=90):
		self.a = a
		self.b = b
	def Area(self):
		return (self.a*self.b)/2
	def Perimeter(self):
		return self.a+self.b+math.sqrt(self.a**2+self.b**2)
		
class Ravnobedrennyj(Triangle):
	def __init__(self, a, alfa):
		self.a = a
		self.alfa = alfa
	def Area(self):
		return (self.a*self.a*math.sin(self.alfa))/2
	def Perimeter(self):
		return 2*self.a+math.sqrt((2*self.a)**2-2*self.a*self.a*math.cos(self.alfa))

class Ravnostoronnyj(Triangle):
	def __init__(self, a, alfa):
		self.a = a
		self.alfa = alfa
	def Area(self):
		return (self.a*self.a*math.sin(self.alfa))/2
	def Perimeter(self):
		return self.a*3