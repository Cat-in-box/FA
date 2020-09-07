import module14
		
cur1 = module14.Dollar(50)
cur2 = module14.Dollar(200)
cur3 = module14.Euro(25)
cur4 = module14.Euro(300)

lst = [cur1, cur2, cur3, cur4]

for i in range(len(lst)):
	lst[i].Calculation()