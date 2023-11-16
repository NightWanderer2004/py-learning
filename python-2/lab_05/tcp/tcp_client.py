# Client
import socket

host = "localhost"
port = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client.sendall("Hehehe...".encode())
data = client.recv(1024)
print(data.decode())

client.close()
