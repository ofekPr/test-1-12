"""EX 2.6 protocol implementation
   Author:Ofek Primor
   Date: 1/11
"""

LENGTH_FIELD_SIZE = 2
PORT = 8820
COMMANDS = ["RAND", "NAME", "TIME", "EXIT"]


def check_cmd(data):
    """Check if the command is defined in the protocol (e.g. RAND, NAME, TIME, EXIT)"""
    return data in COMMANDS, data


def create_msg(data):
    if len(data) < 10:
        return "0" + str(len(data)) + data  # add zero and length to start of message
    elif len(data) < 100:
        return str(len(data)) + data  # add length to start of message
    return "Error: message length too big"


def get_msg(my_socket):
    """Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error" """
    lengt = my_socket.recv(2).decode()  # Get length of message
    if lengt.isnumeric():
        return True, my_socket.recv(int(lengt)).decode()  # Get the context of the message
    return False, "Error"
