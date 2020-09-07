import module10
if __name__ == '__main__':
	fake = module10.Faker(['en_GB'])
	
	Person1 = module10.Plane(fake.name(), random.randint(800, 1000), random.randint(8000, 11000), random.randint(40, 850), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000))
	Person2 = module10.Car(fake.company(), 'P425BP77', fake.year(), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000))
	Person3 = module10.Ship(fake.name(), random.randint(40, 120), fake.random_int(500, 5000), fake.bs(), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000))
	
	lst = [Person1, Person2, Person3]
	for i in range(len(lst)):
		lst[i].Info()
	print('Введите координаты')
	inp_x = int(input('x -> '))
	inp_y = int(input('y -> '))
	inp_z = int(input('z -> '))
	print('\nОтносительно 0, 0, 0 в пределах заданных координат находятся сделующие транспортные средства:\n')
	for i in range(len(lst)):
		if lst[i].Check(inp_x, inp_y, inp_z):
			lst[i].Info()
