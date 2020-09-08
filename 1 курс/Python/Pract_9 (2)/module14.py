import math

class Currency():
	def Calc(self):
		pass
	def Calculation(self):
		pass
		
class Dollar(Currency):
	def __init__(self, d):
		self.d = d
	def Calc(self):
		r = str(self.d*71.54)
		return r[:r.find('.')+4]
	def Calculation(self):
		print(self.d, 'usd =', self.Calc(), 'rub')
		
class Euro(Currency):
	def __init__(self, e):
		self.e = e
	def Calc(self):
		r = str(self.e*80.78)
		return r[:r.find('.')+4]
	def Calculation(self):
		print(self.e,  'eur =', self.Calc(), 'rub')