import module03
spisok1 = module03.Posledovatelnost()

def start():
	print(spisok1.spisok)
	a = input('Желаете создать вложенную последовательность?\n')
	if a == 'да' or a == 'Да':
		a = input('Заполнить ее автоматически?\n')
		if a == 'да' or a == 'Да':
			spisok1.Random_adding()
		elif a == 'нет' or a == 'Нет':
			spisok1.Adding()
		else:
			print('Неизвестная команда')
		start()
	elif a == 'нет' or a == 'Нет':
		pass
	else:
		print('Неизвестная команда')
		start()
		
start()