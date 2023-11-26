# Client
import socket
import dill

host = "localhost"
port = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

data = client.recv(8192)
deserialized_function = dill.loads(data)
result = deserialized_function(2, 2)
print(result)

client.close()