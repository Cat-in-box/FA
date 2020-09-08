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
		