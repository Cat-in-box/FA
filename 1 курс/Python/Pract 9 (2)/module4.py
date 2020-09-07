class Transport():
	def Gruzopodyomnost(self):
		pass
	def Info(self):
		pass
		
class Car(Transport):
	def __init__(self, marka, number, speed, gruzopodyomnost):
		self.marka = marka
		self.number = number
		self.speed = speed
		self.gruzopodyomnost = gruzopodyomnost
	def Info(self):
		print('Автомобиль\nМарка:', self.marka, ' \nНомер:', self.number, ' \nСкорость:', self.speed, ' \nГрузоподъемность:', self.gruzopodyomnost, '\n')
		
class Motorcycle(Transport):
	def __init__(self, marka, number, speed, gruzopodyomnost, kolyaska):
		if kolyaska == False:
			gruzopodyomnost = 0
		self.marka = marka
		self.number = number
		self.speed = speed
		self.gruzopodyomnost = gruzopodyomnost
		self.kolyaska = kolyaska
	def Info(self):
		print('Мотоцикл\nМарка:', self.marka, ' \nНомер:', self.number, ' \nСкорость:', self.speed, ' \nГрузоподъемность:', self.gruzopodyomnost, '\nНаличие коляски:', self.kolyaska, '\n')
		
class Truck(Transport):
	def __init__(self, marka, number, speed, gruzopodyomnost, prizep):
		if prizep == True:
			gruzopodyomnost = gruzopodyomnost*2
		self.marka = marka
		self.number = number
		self.speed = speed
		self.gruzopodyomnost = gruzopodyomnost
		self.prizep = prizep
	def Info(self):
		print('Грузовик\nМарка:', self.marka, ' \nНомер:', self.number, ' \nСкорость:', self.speed, ' \nГрузоподъемность:', self.gruzopodyomnost, '\nНаличие прицепа:', self.prizep, '\n')
