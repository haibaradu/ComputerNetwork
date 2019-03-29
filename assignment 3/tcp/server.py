from socket import *
import threading
import time

serverPort=9999
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))

serverSocket.listen(5)
print("Waiting for connection...")

def tcplink(sock,addr):
    print("Accept new connection from %s:%s..." %addr)
    msg='Welcome!'
    sock.send(msg.encode('utf-8'))
    while True:
        data=sock.recv(1024).decode()
        time.sleep(1)
        if data =='exit' or not data:
            break
        sock.send(('Hello, '+data).encode('utf-8'))
    sock.close()
    print("Connection from %s:%s closed." %addr)

while True:
    sock,addr=serverSocket.accept()
    t=threading.Thread(target=tcplink, args=(sock,addr))
    t.start()
