import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8888

s.connect((host, port))

TEST_REQUEST = b'''GET /test?param1=value1&param2=value2 HTTP/1.1\r
'''

s.send(TEST_REQUEST)
print(str(s.recv(1024)))

s.close()
