import datetime

class Persona:
	def __init__(self, lastname, birthdate):
		self.lastname = lastname
		self.birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
	def Info(self):
		print('Информация о человеке\nФамилия:', self.lastname, '\nДата рождения:', self.birthdate, '\nВозраст:', end = ' '), self.Age()
	def Age(self):
		now = datetime.datetime.now()
		if (now.month, now.day) < (self.birthdate.month, self.birthdate.day):
			print(now.year - self.birthdate.year - 1)
		else:
			print(now.year - self.birthdate.year)

class Abiturient(Persona):
	def __init__(self, lastname, birthdate, fakultet):
		super().__init__(lastname, birthdate)
		self.fakultet = fakultet		
	def Info(self):
		print('Информация о человеке\nФамилия:', self.lastname, '\nФакультет:', self.fakultet,  '\nДата рождения:', self.birthdate, '\nВозраст:', end = ' '), self.Age()
	def Age(self):
		now = datetime.datetime.now()
		if (now.month, now.day) < (self.birthdate.month, self.birthdate.day):
			print(now.year - self.birthdate.year - 1)
		else:
			print(now.year - self.birthdate.year)
		
class Student(Persona):
	def __init__(self, lastname, birthdate, fakultet, kurs):
		super().__init__(lastname, birthdate)
		self.fakultet = fakultet
		self.kurs = kurs
	def Info(self):
		print('Информация о человеке\nФамилия:', self.lastname, '\nФакультет:', self.fakultet, '\nКурс', self.kurs,  '\nДата рождения:', self.birthdate, '\nВозраст:', end = ' '), self.Age()
	def Age(self):
		now = datetime.datetime.now()
		if (now.month, now.day) < (self.birthdate.month, self.birthdate.day):
			print(now.year - self.birthdate.year - 1)
		else:
			print(now.year - self.birthdate.year)
		
class Prepodavatel(Persona):
	def __init__(self, lastname, birthdate, fakultet, dolzhnost, stazh):
		super().__init__(lastname, birthdate)
		self.fakultet = fakultet
		self.dolzhnost = dolzhnost
		self.stazh = stazh
	def Info(self):
		print('Информация о человеке\nФамилия:', self.lastname, '\nФакультет', self.fakultet, '\nДолжность', self.dolzhnost, '\n', self.stazh, '\nДата рождения:', self.birthdate, '\nВозраст:', end = ' '), self.Age()
	def Age(self):
		now = datetime.datetime.now()
		if (now.month, now.day) < (self.birthdate.month, self.birthdate.day):
			print(now.year - self.birthdate.year - 1)
		else:
			print(now.year - self.birthdate.year)

if __name__ == '__main__':
	person1 = Abiturient('Иванов', '5.3.2000', 'ПМиИТ')
	person2 = Student('Петров', '7.10.1999', 'ПМиИТ', '3 курс')
	person3 = Student('Демчук', '14.1.2001', 'ПМиИТ', '1 курс')
	person4 = Prepodavatel('Эмиралиева', '27.6.1968', 'ПМиИТ', 'Преподаватель', '10 лет')
	
	lst = [person1, person2, person3, person4]
	for i in range(len(lst)):
		lst[i].Info()