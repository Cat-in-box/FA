import math

class Progressiya():
	def Calc(self):
		pass
	def Calculation(self):
		pass
		
class Arifmeticheskaya(Progressiya):
	def __init__(self, a1, n, d):
		self.a1 = a1
		self.n = n
		self.d = d
	def N(self):
		return self.a1+(self.n-1)*self.d
	def Summ(self):
		return ((self.a1+self.N())/2)*self.n
	def Prnt(self):
		print(self.Summ())
		
class Geometricheskaya(Progressiya):
	def __init__(self, b1, n, g):
		self.b1 = b1
		self.n = n
		self.g = g
	def N(self):
		print(self.b1*(self.g**(self.n-1)))
	def Summ(self):
		return ((self.b1*((self.g**self.n)-1))/(self.g-1))
	def Prnt(self):
		print(self.Summ())
		
ar = Arifmeticheskaya(2, 5, 7)
ge = Geometricheskaya(4, 6, 8)

lst = [ar, ge]

for i in range(len(lst)):
	lst[i].Prnt()