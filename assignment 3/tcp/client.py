import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 9999))

print (s.recv(1024).decode())

data='HaibaraDu'
s.send(data.encode('utf-8'))
print (s.recv(1024).decode())
s.send('exit'.encode('utf-8'))
s.close()