import socket
import os

global dirname

def process(req):
    if req == 'pwd':
        return dirname
    elif req == 'ls':
        return '; '.join(os.listdir(dirname))
    return 'bad request'


sock = socket.socket()
sock.bind(('', 9090))
sock.listen()
print("Прослушиваем порт")

while True:
    conn, addr = sock.accept()
    
    try:
        dirname = os.path.join(os.getcwd(), r'docs\' + str(addr))
    except:
        os.mkdir(r'docs\' + str(addr))
        dirname = os.path.join(os.getcwd(), r'docs\' + str(addr))

    request = conn.recv(1024).decode()
    print(request)
    
    response = process(request)
    conn.send(response.encode())

conn.close()
