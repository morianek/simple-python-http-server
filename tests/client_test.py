import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8888

s.connect((host, port))
print(str(s.recv(1024)))

s.close()