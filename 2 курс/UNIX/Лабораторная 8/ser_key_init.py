import socket
def get_K():
    f = open(r'C:\Users\anast\Documents\GitHub\pi194-workshoppython-Cat-in-box\5-Task\ser_key.txt', 'r')
    if f.read() == '' or f.read == None:
        f = open(r'C:\Users\anast\Documents\GitHub\pi194-workshoppython-Cat-in-box\5-Task\ser_key.txt', 'w')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('localhost', 8080))
        conn, addr = sock.recvfrom(1024)
        _b = 157
        _g, _p, A = [int(i) for i in conn.decode().split('|')]
        l = open(r'C:\Users\anast\Documents\GitHub\pi194-workshoppython-Cat-in-box\5-Task\license.txt', 'r')
        for line in l:
            if line == str(A):
                B = (_g**_b) % _p
                sock.sendto(str(B).encode(), addr)
                K = (A**_b) % _p
                f.write(str(A)+'\n'+str(K))
                f.close()
                sock.close()
                return K
        sock.close()
        return "Error"
    else:
        f = open(r'C:\Users\anast\Documents\GitHub\pi194-workshoppython-Cat-in-box\5-Task\ser_key.txt', 'r')
        K = 0
        for line in f:
            K = int(line)
        f.close()
        return K