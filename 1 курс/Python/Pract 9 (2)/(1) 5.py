import module05

if __name__ == '__main__':
	person1 = module05.Abiturient('Иванов', '5.3.2000', 'ПМиИТ')
	person2 = module05.Student('Петров', '7.10.1999', 'ПМиИТ', '3 курс')
	person3 = module05.Student('Демчук', '14.1.2001', 'ПМиИТ', '1 курс')
	person4 = module05.Prepodavatel('Эмиралиева', '27.6.1968', 'ПМиИТ', 'Преподаватель', '10 лет')
	
	lst = [person1, person2, person3, person4]
	for i in range(len(lst)):
		lst[i].Info()