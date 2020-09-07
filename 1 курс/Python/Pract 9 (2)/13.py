import module13
		
eq1 = module13.linear('2x=10')
eq2 = module13.linear('2x = 7')
eq3 = module13.quadratic('x^2-2x-3=0')
eq4 = module13.quadratic('x^2 + 12x + 36 = 0')

lst = [eq1, eq2, eq3, eq4]

for i in range(len(lst)):
	lst[i].result()