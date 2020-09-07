class Izdanie():
	def __init__(self, name, author):
		self.name = name
		self.author = author
	def Info(self):
		 return 'Издание\nНазвание: ' + self.name + '\nАвтор: ' + self.author + '\n'
	def author_checker(self, author_input):
		if author_input in self.author:
			return True
		return False

class Kniga(Izdanie):
	def __init__(self, name, author, god, izdatelstvo):
		super().__init__(name, author)
		self.god = god
		self.izdatelstvo = izdatelstvo
	def Info(self):
		return 'Книга\nНазвание: ' + self.name + '\nАвтор: ' + self.author + '\nГод издания: ' + self.god + '\nИздательство: ' + self.izdatelstvo + '\n'
	
class Statya(Izdanie):
	def __init__(self, name, author, name_of_izd, number, god):
		super().__init__(name, author)
		self.name_of_izd = name_of_izd
		self.number = number
		self.god = god
	def Info(self):
		return 'Статья\nНазвание: ' + self.name + '\nАвтор: ' + self.author + '\nНазвание журнала: ' + self.name_of_izd + '\nНомер: ' + self.name_of_izd + '\nГод издания: ' + self.god + '\n'

class Elektronnyj_resurs(Izdanie):
	def __init__(self, name, author, link, annotaziya):
		super().__init__(name, author)
		self.link = link
		self.annotaziya = annotaziya
	def Info(self):
		return 'Электронный ресурс\nНазвание: ' + self.name + '\nАвтор: ' + self.author + '\nСсылка: ' + self.link + '\nАннотация: ' + self.annotaziya + '\n'
