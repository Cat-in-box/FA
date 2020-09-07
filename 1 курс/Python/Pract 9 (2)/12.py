import module12
figure1 = module12.Parallelepiped(5, 7, 10)
figure2 = module12.Shar(4)
figure3 = module12.Piramida(10, 3, 8, 10)
figure4 = module12.Piramida(12, 4, 9, 7)

lst = [figure1, figure2, figure3, figure4]

for i in range(len(lst)):
	lst[i].Info()