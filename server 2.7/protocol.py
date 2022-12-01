#   Ex. 2.7 protocol
import commands
import os

LENGTH_FIELD_SIZE = 4
PORT = 8820


def check_cmd(data):
    valid = True
    valid = valid and data.split(" ")[0] in commands.COMMANDS.keys()

    if data.split(" ")[0] in ["DIR", "COPY", "EXECUTE", "DELETE"]:
        valid = valid and len(data.split(" ")) > 1 and os.path.exists(data.split(" ")[1])

    if data.split(" ")[0] == "COPY":
        valid = valid and len(data.split(" ")) == 3

    if data.split(" ")[0] == "COPY_CLIPBOARD":
        valid = valid and len(data.split(" ")) == 2

    return valid


def create_msg(data):
    return (str(len(str(data))).zfill(LENGTH_FIELD_SIZE) + str(data)).encode()


def get_msg(my_socket):
    lengt = my_socket.recv(LENGTH_FIELD_SIZE).decode()  # Get length of message
    if lengt.isnumeric():
        return True, my_socket.recv(int(lengt)).decode()  # Get the context of the message
    return False, "Error"
