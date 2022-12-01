import socket
import sys

import commands
import protocol

print(sys.argv)

IP = sys.argv[1]
SAVED_PHOTO_LOCATION = sys.argv[2]  # The path + filename where the copy of the screenshot at the client should be saved


def handle_server_response(my_socket, cmd):
    print("handling data with cmd: " + cmd)
    if "SEND_PHOTO" in cmd:  # if sending a photo, large amount of data
        lengthOfLength = my_socket.recv(protocol.LENGTH_FIELD_SIZE).decode()  # Get length of length
        if lengthOfLength.isnumeric():
            lengthOfByte = my_socket.recv(int(lengthOfLength)).decode()  # Get the length of the message
            if lengthOfByte.isnumeric():
                data = my_socket.recv(int(lengthOfByte))  # get all of the content of the image
                while len(data) < int(lengthOfByte):
                    data += my_socket.recv(int(lengthOfByte))
                file = open(SAVED_PHOTO_LOCATION, 'wb')  # open the file and save tha data
                file.write(data)
                file.close()
        return None
    valid, data = protocol.get_msg(my_socket)
    print(data)
    return None
    # (10) treat SEND_PHOTO


def main():
    # open socket with the server
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, protocol.PORT))

    # print instructions
    print('Welcome to remote computer application. Available commands are:\n')
    [print(key) for key in list(commands.COMMANDS.keys())]

    # loop until user requested to exit
    while True:
        try:
            cmd = input("Please enter command:\n")
            if protocol.check_cmd(cmd):
                packet = protocol.create_msg(cmd)
                my_socket.send(packet)
                if cmd == 'EXIT':
                    break
                handle_server_response(my_socket, cmd)
            else:
                print("Not a valid command, or missing parameters\n")
        except:
            pass

    my_socket.close()


if __name__ == '__main__':
    main()
