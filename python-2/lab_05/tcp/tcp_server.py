# Server
import socket

host = "localhost"
port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

while True:
    connection, address = server.accept()
    data = connection.recv(1024)
    connection.sendall(data)
    connection.close()