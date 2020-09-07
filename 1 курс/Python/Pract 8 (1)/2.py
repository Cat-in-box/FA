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

if __name__ == '__main__':

	paper1 = Izdanie('Милионер', 'Еновски')
	paper2 = Kniga('Иммиграция из Англии', 'Спанкулов', '2018', 'Эксмо')
	paper3 = Statya('В мире животных', 'Бэлл', 'Турист', '38', '2020')
	paper4 = Elektronnyj_resurs('Мороженное', 'Википедия', 'https://vk.cc/apEosC', 'Мороженое — пищевой продукт-десерт, представляющий собой замороженную в процессе непрерывного взбивания массу, содержащую в основе своей питательные, вкусовые, ароматические и эмульгирующие вещества. К мороженому нередко относят также фруктовый лёд, получаемый простым замораживанием фруктово-ягодных соков и пюре (из апельсина чаще всего делают фруктовый лёд).')
	
	lst = [paper1, paper2, paper3, paper4]
	for i in range(len(lst)):
		print(lst[i].Info())
	
	author_input = input('Поиск по автору. Введите автора: ')
	flag = False
	for i in range(len(lst)):
		if lst[i].author_checker(author_input) == True:
			print(lst[i].Info())
			flag = True
	if not flag:
		print('Ничего не найдено')