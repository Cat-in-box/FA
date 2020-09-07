from faker import Faker
import datetime

class Software():
	def Info(self):
		pass
	def Check(self):
		if int(str(self.date_end).replace('-', '')) <= int(str(datetime.datetime.now())[0:8].replace('-', '')):
			return True
		else:
			return False

class Free(Software):
	def __init__(self, name, developer):
		self.name = name
		self.developer = developer
		self.date_end = str(datetime.datetime.now())[0:8]
	def Info(self):
		print('Бесплатное ПО\nНазвание:', self.name, '\nПроизводитель:', self.developer, '\n')
	
class Shareware(Software):
	def __init__(self, name, developer, date, free_use_period):
		self.name = name
		self.developer = developer
		self.date = date
		self.free_use_period = free_use_period
		self.date_end = self.date[0: self.date.find('-')] + '-' + str(int(self.date[self.date.find('-')+1: self.date.find('-')+3]) + int(self.free_use_period)) + '-' + self.date[self.date.find('-')+4:]
	def Info(self):
		print('Условно бесплатное ПО\nНазание:', self.name, '\nПроизводитель:', self.developer, '\nДата установки:', self.date, '\nСрок бесплатного использования:', self.free_use_period, '\n')

class Commercial(Software):
	def __init__(self, name, developer, price, date, use_period):
		self.name = name
		self.developer = developer
		self.price = price
		self.date = date
		self.use_period = use_period
		self.date_end = self.date[0: self.date.find('-')] + '-' + str(int(self.date[self.date.find('-')+1: self.date.find('-')+3]) + int(self.use_period)) + '-' + self.date[self.date.find('-')+4:]
	def Info(self):
		print('Коммерческое ПО\nНазвание:', self.name, '\nПроизводитель:', self.developer, '\nЦена:', self.price, '\nДата установки:', self.date, '\nСрок использования:', self.use_period, '\n')

if __name__ == '__main__':
	fake = Faker(['en_GB'])
	
	Person1 = Free(fake.catch_phrase(), fake.company())
	Person2 = Shareware(fake.catch_phrase(), fake.company(), fake.date(), fake.month())

	Person3 = Commercial(fake.catch_phrase(), fake.company(), fake.random_int(500, 5000), fake.date(), fake.month())
	
	lst = [Person1, Person2, Person3]
	for i in range(len(lst)):
		lst[i].Info()

	print('На данный момент актуально следующее ПО:\n')
	for i in range(len(lst)):
		if lst[i].Check():
			lst[i].Info()
