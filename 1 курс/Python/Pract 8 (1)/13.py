import math

class equation():
	def calculation(self):
		pass
	def result(self):
		return calculation(self)

class linear(equation):
	def __init__(self, inp):
		x = inp[0:inp.find('x')].replace(' ', '')
		r = inp[inp.find('=')+1:].replace(' ', '')
		self.x = int(x)
		self.r = int(r)
	def calculation(self):
		return 'x = ' + str(self.r/self.x)
	def result(self):
		print(self.calculation())

class quadratic(equation):
	def __init__(self, inp):
		a = 1
		inp = inp[inp.find('x^2')+3:].replace(' ', '')
		b = inp[: inp.find('x')].replace(' ', '')
		c = inp[inp.find('x')+1: inp.find('=')].replace(' ', '')
		self.a = int(a)
		self.b = int(b)
		self.c = int(c)
	def calculation(self):
		D = self.b*self.b-4*self.a*self.c
		if (D)>0:
			return 'x1 = ' + str((-self.b+math.sqrt(D))/(2*self.a)) + '\nx2 = ' + str((-self.b-math.sqrt(D))/(2*self.a))
		elif (D)==0:
			return 'x = ' + str((-self.b)/(2*self.a))
		else:
			return 'корней нет'
	def result(self):
		print(self.calculation())
		
eq1 = linear('2x=10')
eq2 = linear('2x = 7')
eq3 = quadratic('x^2-2x-3=0')
eq4 = quadratic('x^2 + 12x + 36 = 0')

lst = [eq1, eq2, eq3, eq4]

for i in range(len(lst)):
	lst[i].result()