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

triangle1 = Triangle(5, 7, 30)
triangle2 = Pryamougolnyj(10, 12)
triangle3 = Ravnobedrennyj(3, 50)
triangle4 = Ravnostoronnyj(20, 120)

lst = [triangle1, triangle2, triangle3, triangle4]

for i in range(len(lst)):
	lst[i].Info()