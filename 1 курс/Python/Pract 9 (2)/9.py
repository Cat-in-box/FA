import module9
if __name__ == '__main__':
	fake = module9.Faker(['en_GB'])
	
	Person1 = module9.Free(fake.catch_phrase(), fake.company())
	Person2 = module9.Shareware(fake.catch_phrase(), fake.company(), fake.date(), fake.month())

	Person3 = module9.Commercial(fake.catch_phrase(), fake.company(), fake.random_int(500, 5000), fake.date(), fake.month())
	
	lst = [Person1, Person2, Person3]
	for i in range(len(lst)):
		lst[i].Info()

	print('На данный момент актуально следующее ПО:\n')
	for i in range(len(lst)):
		if lst[i].Check():
			lst[i].Info()
