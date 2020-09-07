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

transport1 = Car('BMW', 'A666PY66', 220, 1500)
transport2 = Motorcycle('Mercedes', 'E123cc177', 100, 200, True)
transport3 = Motorcycle('Volkswagen', 'P259PP150', 90, 250, False)
transport4 = Truck('MAN', 'P425BP77', 120, 15000, True)
transport5 = Truck('KAMAZ', 'B093OP777', 100, 25000, False)

lst = [transport1, transport2, transport3, transport4, transport5]
for i in range(len(lst)):
	lst[i].Info()