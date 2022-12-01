"""EX 2.6 client implementation
   Author: Ofek Primor
   Date: 1/11
"""

import socket
import protocol


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("127.0.0.1", protocol.PORT))

    while True:
        user_input = input("Enter command\n")
        # Check if user entered a valid command as defined in protocol
        valid_cmd = protocol.check_cmd(user_input)

        if valid_cmd:
            # If the command is valid:
            # 1. Add length field ("RAND" -> "04RAND")
            user_input = protocol.create_msg(user_input)
            # 2. Send it to the server
            my_socket.send(user_input.encode())
            # 3. If command is EXIT, break from while loop
            if "EXIT" in user_input:
                break
            # 4. Get server's response
            data = my_socket.recv(1024).decode()
            # 5. If server's response is valid, print it
            if data:
                print(data)
            else:
                print("Response not valid\n")
        else:
            print("Not a valid command")

    print("Closing\n")
    # Close socket
    my_socket.close()


if __name__ == "__main__":
    main()
