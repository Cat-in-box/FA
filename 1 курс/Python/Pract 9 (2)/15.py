import module15
		
ar = module15.Arifmeticheskaya(2, 5, 7)
ge = module15.Geometricheskaya(4, 6, 8)

lst = [ar, ge]

for i in range(len(lst)):
	lst[i].Prnt()