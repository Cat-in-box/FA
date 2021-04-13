import socket

class Client():
    def __init__(self):
        self.server = 'localhost', 9090  # Данные сервера
        self.sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sor.bind(('', 0)) # Задаем сокет как клиент
        self.auth = False
        self.name = None

    def read_sok(self):
        while 1 :
            data = self.sor.recv(1024)
            print(data.decode('utf-8'))

    def login(self):
        self.sor.sendto(str.encode('Connect to server'), self.server) #Уведомляем сервер о подключении
        a = self.sor.recv(1024).decode()
        if a == 'Жду регистрацию':
            self.sor.sendto(str.encode(input('Введите ваш логин: ')), self.server)
            self.sor.sendto(str.encode(input('Введите ваш пароль: ')), self.server)
            a = self.sor.recv(1024).decode()
            if a != 'False':
                print('зарегались')
                self.auth = True
                self.name = a
            else:
                self.auth = False
        else:
            print('Привет,', a)
            a = self.sor.recv(1024).decode()
            while a == 'Жду пароль':
                self.sor.sendto(str.encode(input('Введите пароль: ')), self.server)
                a = self.sor.recv(1024).decode()
            self.auth = True
            self.name = a

Client_new = Client()
Client_new.login()
inp = input('Введите сообщение: ')

while inp != 'exit':
    msg = '[' + Client_new.name + '] ' + inp
    Client_new.sor.sendto(msg.encode(), Client_new.server)
    data = Client_new.sor.recv(1024)
    print(data.decode())
    inp = input('Введите сообщение: ')

print('вышли')
Client_new.sor.close()