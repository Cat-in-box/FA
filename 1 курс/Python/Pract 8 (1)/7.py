from faker import Faker

class Telephone_book():
	def Info(self):
		pass
	def Search(self, inp_lastname):
		if self.lastname == inp_lastname:
			return True
		else:
			return False

class Person(Telephone_book):
	def __init__(self, lastname, address, number):
		self.lastname = lastname
		self.address = address
		self.number = number
	def Info(self):
		print('Персона\nФамилия:', self.lastname, '\nАдрес:', self.address, '\nНомер телефона:', self.number, '\n')
	
class Organisation(Telephone_book):
	def __init__(self, name, address, number, fax, lastname):
		self.name = name
		self.address = address
		self.number = number
		self.fax = fax
		self.lastname = lastname
	def Info(self):
		print('Организация\nНазвание:', self.name, '\nАдрес:', self.address, '\nНомер телефона:', self.number, '\nФакс:', self.fax, '\nКонтактное лицо:', self.lastname, '\n')
	
class Friend(Telephone_book):
	def __init__(self, lastname, address, number, birthdate):
		self.lastname = lastname
		self.address = address
		self.number = number
		self.birthdate = birthdate
	def Info(self):
		print('Друг\nФамилия:', self.lastname, '\nАдрес:', self.address, '\nНомер телефона:', self.number, '\nДата рождения:', self.birthdate, '\n')
		
if __name__ == '__main__':
	fake = Faker(['ru_RU'])
	
	Person1 = Person(fake.last_name(), fake.address(), fake.phone_number())
	Person2 = Organisation(fake.company(), fake.address(), fake.phone_number(), fake.phone_number(), fake.last_name())
	Person3 = Friend(fake.last_name(), fake.address(), fake.phone_number(), fake.date())
	
	lst = [Person1, Person2, Person3]
	for i in range(len(lst)):
		lst[i].Info()
		
	inp_lastname = input('Введите фамилию: ')
	print('Результаты по вашему запросу:\n')
	for i in range(len(lst)):
		if lst[i].Search(inp_lastname):
			lst[i].Info()