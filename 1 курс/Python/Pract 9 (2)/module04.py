import math

class f:
	def __init__(self, x):
		self.x = x
	def Function(self):
		print(((self.x+math.sin(self.x))**(1/3))/(self.x**2-self.x**4)*(math.asin((3-self.x)**(1/4)))**(1/2))
		