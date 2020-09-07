import module11
if __name__ == '__main__':
	fake = module11.Faker(['en_GB'])
	
	Person1 = module11.Cube(fake.color_name(), random.randint(50, 500), 'пластмасса', random.randint(2, 20))
	Person2 = module11.Ball(fake.color_name(), random.randint(50, 1500), 'полимер', random.randint(20, 1000))
	Person3 = module11.Car(fake.name(), fake.color_name(), fake.random_int(300, 5000), fake.company())
	
	lst = [Person1, Person2, Person3]
	for i in range(len(lst)):
		lst[i].Info()

	inp = input('Введите цвет: ')
	print('По ашему запросу нашлось:\n')
	for i in range(len(lst)):
		if lst[i].Check(inp):
			lst[i].Info()
