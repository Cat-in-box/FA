import socket

server = 'localhost', 9090

while True:
    request = input('>')
    
    sock = socket.socket()
    sock.connect(server)
    
    sock.send(request.encode())
    
    response = sock.recv(1024).decode()
    print(response)
    
    sock.close()