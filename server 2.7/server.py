import socket
import sys

import commands
import protocol

IP = sys.argv[1]
PHOTO_PATH = sys.argv[2]  # The path + filename where the screenshot at the server should be saved


def check_client_request(cmd):
    if not protocol.check_cmd(cmd):
        return False, "Not valid", []
    return True, cmd.split(" ", 1)[0], cmd.split(" ")[1:]  # returns valid, command and params


def handle_client_request(command, params):
    print(f"{command=} , {params=}")
    response = commands.COMMANDS[command](params)  # calls the function through a dictionary
    return response


def main():
    # open socket with client
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, protocol.PORT))

    while True:
        server_socket.listen()
        print("Server is up and running")
        (client_socket, client_address) = server_socket.accept()
        print("Client connected")

        # handle requests until user asks to exit
        while True:
            try:
                valid_protocol, cmd = protocol.get_msg(client_socket)
                if valid_protocol:
                    # Check if params are good, e.g. correct number of params, file name exists
                    valid_cmd, command, params = check_client_request(cmd)
                    if valid_cmd:
                        if command == 'EXIT':
                            # close socket
                            print("Closing connection")
                            client_socket.close()
                            break
                        # prepare a response using "handle_client_request"
                        print(valid_cmd, command, params)
                        response = handle_client_request(command, params)
                        if 'SEND_PHOTO' not in command:
                            # add length field using "create_msg"
                            response = protocol.create_msg(response)
                            # send to client
                            client_socket.send(response)
                        elif command == 'SEND_PHOTO':
                            # Send the data itself to the client
                            client_socket.send(response[0].encode())
                            client_socket.sendall(response[1])
                    else:
                        # prepare proper error to client
                        response = 'Bad command or parameters'
                        # send to client
                        client_socket.send(protocol.create_msg(response))
                else:
                    # prepare proper error to client
                    response = 'Packet not according to protocol'
                    # send to client
                    client_socket.send(protocol.create_msg(response))

                    # Attempt to clean garbage from socket
                    client_socket.recv(1024)
            except:
                pass


if __name__ == '__main__':
    main()
