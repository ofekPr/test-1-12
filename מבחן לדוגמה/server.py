import socket
import re

regex = '\d+ [+\-*/] \d+'
actions = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y
}

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen()
print("Server is up and running")

(client_socket, client_address) = server_socket.accept()
print("Client connected")

while True:
    data = client_socket.recv(1024).decode()
    print("Client sent: " + data)

    if data == "EXIT":
        break

    if re.match(regex, data):
        print(data)
        data = data.split(' ')
        reply = actions[data[1]](int(data[0]), int(data[2]))
    else:
        reply = "Not valid!"

    client_socket.send(str(reply).encode())

client_socket.close()
server_socket.close()
