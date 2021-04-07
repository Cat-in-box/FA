import socket
import threading
 
class T(threading.Thread):
	def __init__(self, n):
		self.n = str(n)
		threading.Thread.__init__(self, name="t" + self.n)
	def run(self):
		print("Процесс", self.n)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			msg = data.decode()
			conn.send(data)
			print(msg)

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)

counter = 0
while True:
	
	conn, addr = sock.accept()
	print(addr)
	counter += 1
	p = T(counter)
	p.start()

conn.close()
