# Server
import socket

host = "localhost"
port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))

while True:
    data, address = server.recvfrom(1024)
    server.sendto(data, address)