import module5
if __name__ == '__main__':
	fake = module5.Faker(['ru_RU'])
	Item1 = module5.Product(fake.word(), random.randint(100, 5000), fake.date(), str(random.randint(1, 24))+' месяцев')
	Item2 = module5.Consignment(fake.word(), random.randint(100, 5000), random.randint(100, 1000), fake.date(), str(random.randint(1, 24))+' месяцев')
	Item3 = module5.Phone(fake.word(), random.randint(500, 100000))
	Item4 = module5.Phone(fake.word(), random.randint(500, 100000))
	
	lst = [Item1, Item2, Item3, Item4]
	for i in range(len(lst)):
		lst[i].Info()
	money = int(input('Введите максимальную сумму, на которую хотите сделать заказ: '))
	print('Вы можете позволить себе следующие товары:\n')
	for i in range (len(lst)):
		if lst[i].Purchase(money):
			lst[i].Info()