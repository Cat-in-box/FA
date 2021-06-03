import socket
def get_K():
    f = open(r'C:\Users\anast\Documents\GitHub\pi194-workshoppython-Cat-in-box\5-Task\cli_key.txt', 'r')
    if f.read() == '' or f.read == None:
        f = open(r'C:\Users\anast\Documents\GitHub\pi194-workshoppython-Cat-in-box\5-Task\cli_key.txt', 'w')
        server = 'localhost', 8080  # Данные сервера
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.bind(('', 0)) # Задаем сокет как клиент

        _a = 199
        _g = 197
        _p = 151
        A = (_g**_a) % _p

        msg = str(_g)+'|'+str(_p)+'|'+str(A)
        sock.sendto(msg.encode(), server)
        B = int(sock.recv(1024).decode())
        K = (B**_a) % _p
        f.write(str(A)+'\n'+str(K))
        f.close()
        sock.close()
        return K
    else:
        f = open(r'C:\Users\anast\Documents\GitHub\pi194-workshoppython-Cat-in-box\5-Task\cli_key.txt', 'r')
        K = 0
        for line in f:
            K = int(line)
        f.close()
        return K