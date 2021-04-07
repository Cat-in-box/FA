import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
print('SYS: Соединение с сервером')
sock.connect((input('Введите имя хоста: '), int(input('Введите номер порта: '))))

msg = ''

while msg != 'exit':
    msg = input('Введите сообщение: ')
    print('SYS: Отправка данных серверу')
    sock.send(msg.encode())

    print('SYS: Прием данных от сервера')
    data = sock.recv(1024)
    print(data.decode())

print('SYS: Разрыв соединения с сервером')
sock.close()
