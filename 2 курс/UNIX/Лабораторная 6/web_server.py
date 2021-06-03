from socket import socket
from threading import Thread, Lock
from datetime import datetime


class Client(Thread):
    def __init__(self, addr, conn):
        Thread.__init__(self, name=str(addr[0]) + " " + str(addr[1]))
        self.host = addr[0]
        self.port = addr[1]
        self.conn = conn

    def run(self):
        """Старт сервера"""
        request = self.conn.recv(DATA_SIZE).decode()
        if request != '':
            print(request)

            headers = request.split('\n')
            webpage = headers[0].split()[1]
            if webpage == '/':
                webpage = '/index.html'
            elif '.' not in webpage:
                webpage += '.html'

            if webpage.split('.')[-1] in FILES:
                try:
                    try:
                        with open(DEFAULT_FOLDER + webpage, 'r') as f:
                            content = f.read()
                        response = """HTTP/1.1 200 OK
                                Server: WebServer
                                Content-type: text/html
                                Content-length: 5000
                                Connection: close\n\n""" + content
                    except UnicodeDecodeError:
                        # 8. бинарный тип
                        with open(DEFAULT_FOLDER + webpage, 'rb') as f:
                            content = f.read()
                        response = """HTTP/1.1 200 OK
                                Server: WebServer
                                Content-type: image\png
                                Content-length: 5000
                                Connection: close\n\n"""
                    with lock:
                        with open('log.txt', 'a+') as log:
                            log.write(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + ' | ' + self.host
                                      + ' | ' + webpage + ' | None\n')

                except FileNotFoundError:
                    # 3. Ошибка 404
                    response = 'HTTP/1.0 404 NOT FOUND\n\nPage Not Found!'
                    with lock:
                        with open('log.txt', 'a+') as log:
                            log.write(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + ' | ' +
                                      self.host + ' | ' + webpage + ' | 404\n')
            
                if "Content-type: image\png" in response:
                    self.conn.sendall(response.encode()+content)
                else:
                    self.conn.sendall(response.encode())

            else:
                # 6. Тип файлов
                if webpage.split('.')[-1] != "ico":
                    response = 'HTTP/1.0 403 FORBIDDEN\n\nForbidden Error!'
                    with lock:
                        with open('log.txt', 'a+') as log:
                            log.write(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + ' | ' +
                                      self.host + ' | ' + webpage + ' | 403\n')

        self.conn.close()


config = {}
with open('server_config.txt', 'r') as f:
    for i in f.readlines():
        config[i.split("=")[0]] = i.split("=")[1]
SERVER_HOST = config['DEFAULT_HOST'].strip()
SERVER_PORT = int(config['DEFAULT_PORT'])
DATA_SIZE = int(config['DATA_SIZE'])
DEFAULT_FOLDER = config['DEFAULT_FOLDER'].strip()
# 6. определенные типы
FILES = ['html', 'js', 'png', 'jpg', 'jpeg']

sock = socket()
sock.bind((SERVER_HOST, SERVER_PORT))
sock.listen(3)
lock = Lock()

clients = []
while True:
    try:
        conn, addr = sock.accept()
        clients.append(Client(addr, conn))
        clients[-1].start()

        for cl in clients:
            if not cl.is_alive():
                clients.remove(cl)
    except:
        break

sock.close()
