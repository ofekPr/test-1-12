"""EX 2.6 server implementation
   Author: Ofek Primor
   Date: 1/11
"""

import socket
import protocol
import datetime
import random

NAME = "OFEK"


def create_server_rsp(cmd):
    """Based on the command, create a proper response"""
    if cmd == "TIME":
        return str(datetime.datetime.now())  # return time
    elif cmd == "NAME":
        return NAME  # return name
    elif cmd == "RAND":
        return str(random.randint(1, 10))  # return random number between 1-10


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", protocol.PORT))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    while True:
        # Get message from socket and check if it is according to protocol
        valid_msg, cmd = protocol.get_msg(client_socket)
        if valid_msg:
            # 1. Print received message
            print(cmd)
            # 2. Check if the command is valid
            valid_data, data = protocol.check_cmd(cmd)
            # 3. If valid command - create response
            if valid_data:
                response = create_server_rsp(cmd)
            else:
                response = "Wrong command"
        else:
            response = "Wrong protocol"
            client_socket.recv(1024)  # Attempt to empty the socket from possible garbage
        # Handle EXIT command, no need to respond to the client
        if cmd == "EXIT":
            break
        # Send response to the client
        client_socket.send(response.encode())

    print("Closing\n")
    # Close sockets
    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    main()
