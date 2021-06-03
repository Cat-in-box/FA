import socket
from time import sleep
from random import random

import cli_key_init
import encryption as enc

K = cli_key_init.get_K()

server = 'localhost', 9090  # Данные сервера
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('', 0)) # Задаем сокет как клиент

msg = "Подключились?"
print(msg)
sock.sendto(enc.dh_encrypt(msg, K).encode(), server)
print(enc.dh_decrypt(sock.recv(1024).decode(), K))
