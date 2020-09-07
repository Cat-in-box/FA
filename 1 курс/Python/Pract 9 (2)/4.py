import module4
transport1 = module4.Car('BMW', 'A666PY66', 220, 1500)
transport2 = module4.Motorcycle('Mercedes', 'E123cc177', 100, 200, True)
transport3 = module4.Motorcycle('Volkswagen', 'P259PP150', 90, 250, False)
transport4 = module4.Truck('MAN', 'P425BP77', 120, 15000, True)
transport5 = module4.Truck('KAMAZ', 'B093OP777', 100, 25000, False)

lst = [transport1, transport2, transport3, transport4, transport5]
for i in range(len(lst)):
	lst[i].Info()