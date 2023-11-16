# Client
import socket

host = "localhost"
port = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Hey, from client!".encode(), (host, port))

data, address = client.recvfrom(1024)

print(data.decode())