import socket
import sys

def file_writer(m):
	log_file = open('C:/Users/anast/Desktop/1/log_file.txt', 'a')
	log_file.write(m, '\n')
	log_file.close()

file_writer('SYS: Запуск сервера\n')

sock = socket.socket()
sock.bind(('', int(input('Введите номер порта: '))))

while True:
	file_writer('SYS: Начало прослушивания порта\n')
	sock.listen(1)
	file_writer('SYS: Подключение клиента\n')
	conn, addr = sock.accept()
	file_writer('Подключились к' + str(addr))

	msg = ''

	file_writer('SYS: Прием данных от клиента\n')
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg = data.decode()
		file_writer('SYS: Отправка данных клиенту\n')
		conn.send(data)
		file_writer('Отправили' + str(msg) + '\n')

	file_writer('SYS: Отключение клиента\n')
	conn.close()