import socket
from time import sleep
import scanner

sock = socket.socket()
sock.setblocking(1)
scanner.scann()

#msg = input()
msg = "Hi!"
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
