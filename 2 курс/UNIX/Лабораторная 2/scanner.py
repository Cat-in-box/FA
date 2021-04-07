import socket
from threading import Thread

N = 2**16 - 1
host = input('Введите имя хоста/IP-адрес')

for port in range(1,100):
    sock = socket.socket()
    try:
        print(port)
        sock.connect((host, port))
        print("Порт", i, "открыт")
    except:
        continue
    finally:
        sock.close()