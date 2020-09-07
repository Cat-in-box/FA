import module3

triangle1 = module3.Triangle(5, 7, 30)
triangle2 = module3.Pryamougolnyj(10, 12)
triangle3 = module3.Ravnobedrennyj(3, 50)
triangle4 = module3.Ravnostoronnyj(20, 120)

lst = [triangle1, triangle2, triangle3, triangle4]

for i in range(len(lst)):
	lst[i].Info()