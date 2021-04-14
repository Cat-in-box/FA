import socket
import threading
from threading import Thread
import time
 
class T(threading.Thread):
    def __init__(self, Number_all, n, host):
        self.Number_all = Number_all
        self.n = n
        self.host = host
        self.progress = 0
        threading.Thread.__init__(self, name="t" + str(self.n))
	
    def run(self):
        print("Процесс", self.n)
        K = self.n*10000
        if K > self.Number_all:
            K = (self.n-1)*10000 - self.Number_all

        for port in range((self.n-1)*10000 + 1, K):
            sock = socket.socket()
            self.progress = port - (self.n-1)*10000 + 1
            try:
                print(port)
                sock.connect((self.host, port))
                print("Порт", port, "открыт")
            except:
                continue

def scann():
    Number_all = 2**16 - 1
    #p_list = []
    host = input('Введите имя хоста/IP-адрес')
    for p_number in range(Number_all // 10000 + 1):
        p = T(Number_all, p_number+1, host)
        #p_list.append(p)
        p.start()
    
    '''
    flag = True
    while flag:
        count = round(100*sum(p.progress for p in p_list)/Number_all, 2)
        if count == 100.0:
            flag = False
        print("Прогресс: " + str(count) + '%')
        time.sleep(5)
    '''
