# Server
import socket
import dill

host = "localhost"
port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

def func(a, b):
    print("Hello from func")
    return a + b

while True:
    connection, address = server.accept()
    
    serialized_function = dill.dumps(func)
    connection.sendall(bytes(serialized_function))
    
    connection.close()