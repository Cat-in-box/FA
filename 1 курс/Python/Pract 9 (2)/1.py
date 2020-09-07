import module1
figure1 = module1.Circle(5)
figure2 = module1.Rectangle(7, 4)
figure3 = module1.Triangle(10, 3, 8)
figure4 = module1.Triangle(12, 4, 9)

lst = [figure1, figure2, figure3, figure4]

for i in range(len(lst)):
	lst[i].Info()