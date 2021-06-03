import socket
import sys

import ser_key_init
import encryption as enc

print ('Start Server')

K = ser_key_init.get_K()
if K == "Error":
    print("Доступ запрещен")
    exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 9090))

conn, addr = sock.recvfrom(1024)
print('Подключились к' + str(addr))

msg = enc.dh_decrypt(conn.decode(), K)
print(msg)
msg = msg[:-1] + '!'

sock.sendto(enc.dh_encrypt(msg, K).encode(), addr)
print(msg)