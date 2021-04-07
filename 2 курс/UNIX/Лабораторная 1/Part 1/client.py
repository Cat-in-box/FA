import socket
from time import sleep

def file_writer(m):
	log_file = open('C:/Users/anast/Desktop/1/log_file.txt', 'a')
	log_file.write('SYS', m, '\n')
	log_file.close()

sock = socket.socket()
sock.setblocking(1)
file_writer('SYS: Соединение с сервером')
sock.connect((input('Введите имя хоста: '), int(input('Введите номер порта: '))))

msg = ''

while msg != 'exit':
    msg = input('Введите сообщение: ')
    file_writer('SYS: Отправка данных серверу')
    sock.send(msg.encode())

    file_writer('SYS: Прием данных от сервера')
    data = sock.recv(1024)
    file_writer(data.decode())

file_writer('SYS: Разрыв соединения с сервером')
sock.close()
