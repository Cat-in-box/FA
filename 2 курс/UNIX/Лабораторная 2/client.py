import socket
from time import sleep
import os

sock = socket.socket()
sock.setblocking(1)
os.system('python scanner.py')

'''
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
'''

#msg = input()
msg = "Hi!"
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())