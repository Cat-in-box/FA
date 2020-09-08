import module6

if __name__ == '__main__':
	fake = module6.Faker(['ru_RU'])
	item1 = module6.Toy('Мишка', 800, 'Aurora', 'трикотаж, поролон', 2)
	item2 = module6.Toy('Lego Friends', 1000, 'Lego', 'пластмасса', 5)
	item3 = module6.Book('Стихи для детей', 'Агния Барто', 180, 'Эксмо', 3)
	item4 = module6.Book('Хорошо быть тихоней', 'Стивен Чбоски', 315, 'Азбука', 18)
	item5 = module6.Sport_equipment('Горные лыжи', 1500, 'Атомик', 10)
	item6 = module6.Sport_equipment('Гантели', 190, 'York fitness', 15)
	
	lst = [item1, item2, item3, item4, item5, item6]
	for i in range(len(lst)):
		lst[i].Info()
	age = int(input('Введите возраст: '))
	print('Вы можете позволить себе следующие товары:\n')
	for i in range (len(lst)):
		if lst[i].Purchase(age):
			lst[i].Info()