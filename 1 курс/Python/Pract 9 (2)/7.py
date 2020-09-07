import module7
if __name__ == '__main__':
	fake = Faker(['ru_RU'])
	
	Person1 = module7.Person(fake.last_name(), fake.address(), fake.phone_number())
	Person2 = module7.Organisation(fake.company(), fake.address(), fake.phone_number(), fake.phone_number(), fake.last_name())
	Person3 = module7.Friend(fake.last_name(), fake.address(), fake.phone_number(), fake.date())
	
	lst = [Person1, Person2, Person3]
	for i in range(len(lst)):
		lst[i].Info()
		
	inp_lastname = input('Введите фамилию: ')
	print('Результаты по вашему запросу:\n')
	for i in range(len(lst)):
		if lst[i].Search(inp_lastname):
			lst[i].Info()