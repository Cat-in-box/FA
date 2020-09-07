import module8
if __name__ == '__main__':
	fake = module8.Faker(['ru_RU'])
	
	Person1 = module8.Depositor(fake.last_name(), fake.date(), fake.random_int(500, 999999999), fake.random_int(1, 99))
	Person2 = module8.Creditor(fake.last_name(), fake.date(), fake.random_int(500, 999999999), fake.random_int(1, 99), fake.random_int(500, 999999999))
	Person3 = module8.Company(fake.company(), fake.date(), fake.random_int(10000000000000000000, 99999999999999999999), fake.random_int(10000, 999999999999))
	
	lst = [Person1, Person2, Person3]
	for i in range(len(lst)):
		lst[i].Info()
		
	inp_date = input('Введите дату начала сотрудничества: ')
	print('Результаты по вашему запросу:\n')
	for i in range(len(lst)):
		if lst[i].Search(inp_date):
			lst[i].Info()