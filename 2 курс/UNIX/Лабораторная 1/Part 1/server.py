import socket
from threading import Timer

def stop():
	log_file.write('SYS: Остановка сервера')
	log_file.close()
	exit(0)

log_file = open('./log_file.txt', 'w')

log_file.write('SYS: Запуск сервера')
sock = socket.socket()
sock.bind(('', int(input('Введите номер порта: '))))
while True:
	log_file.write('SYS: Начало прослушивания порта')
	sock.listen(1)
	timeout = 10
	t = Timer(timeout, stop)
	t.start()
	log_file.write('SYS: Подключение клиента')
	conn, addr = sock.accept()
	t.cancel()
	print(addr)

	msg = ''

	log_file.write('SYS: Прием данных от клиента')
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		log_file.write('SYS: Отправка данных клиенту')
		conn.send(data)

	print(msg)

	log_file.write('SYS: Отключение клиента')
	conn.close()