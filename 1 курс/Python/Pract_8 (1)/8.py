from faker import Faker

class Client():
	def Info(self):
		pass
	def Search(self, inp_date):
		if self.date == inp_date:
			return True
		else:
			return False

class Depositor(Client):
	def __init__(self, lastname, date, size, procent):
		self.lastname = lastname
		self.date = date
		self.size = size
		self.procent = procent
	def Info(self):
		print('Вкладчик\nФамилия:', self.lastname, '\nДата открытия вклада:', self.date,  '\nРазмер вклада:', self.size, '\nПроцент по вкладу:', str(self.procent)+'%', '\n')
	
class Creditor(Client):
	def __init__(self, lastname, date, size, procent, balance_owed):
		self.lastname = lastname
		self.date = date
		self.size = size
		self.procent = procent
		self.balance_owed = balance_owed
	def Info(self):
		print('Кредитор\nФамилия:', self.lastname, '\nДата открытия вклада:', self.date, '\nРазмер кредита:', self.size, '\nПроцент по кредиту:', str(self.procent)+'%', '\nОстаток долга:', self.balance_owed, '\n')
	
class Company(Client):
	def __init__(self, lastname, date, number, balance):
		self.lastname = lastname
		self.date = date
		self.number = number
		self.balance = balance
	def Info(self):
		print('Организация\nНазвание:', self.lastname, '\nДата открытия счета:', self.date, '\nНомер счета:', self.number, '\nСумма на счету:', self.balance, '\n')
		
if __name__ == '__main__':
	fake = Faker(['ru_RU'])
	
	Person1 = Depositor(fake.last_name(), fake.date(), fake.random_int(500, 999999999), fake.random_int(1, 99))
	Person2 = Creditor(fake.last_name(), fake.date(), fake.random_int(500, 999999999), fake.random_int(1, 99), fake.random_int(500, 999999999))
	Person3 = Company(fake.company(), fake.date(), fake.random_int(10000000000000000000, 99999999999999999999), fake.random_int(10000, 999999999999))
	
	lst = [Person1, Person2, Person3]
	for i in range(len(lst)):
		lst[i].Info()
		
	inp_date = input('Введите дату начала сотрудничества: ')
	print('Результаты по вашему запросу:\n')
	for i in range(len(lst)):
		if lst[i].Search(inp_date):
			lst[i].Info()