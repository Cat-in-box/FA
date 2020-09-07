import module2
if __name__ == '__main__':

	paper1 = module2.Izdanie('Милионер', 'Еновски')
	paper2 = module2.Kniga('Иммиграция из Англии', 'Спанкулов', '2018', 'Эксмо')
	paper3 = module2.Statya('В мире животных', 'Бэлл', 'Турист', '38', '2020')
	paper4 = module2.Elektronnyj_resurs('Мороженное', 'Википедия', 'https://vk.cc/apEosC', 'Мороженое — пищевой продукт-десерт, представляющий собой замороженную в процессе непрерывного взбивания массу, содержащую в основе своей питательные, вкусовые, ароматические и эмульгирующие вещества. К мороженому нередко относят также фруктовый лёд, получаемый простым замораживанием фруктово-ягодных соков и пюре (из апельсина чаще всего делают фруктовый лёд).')
	
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