from scapy.all import *
from scapy.layers.dns import *

MOVE_PORT = 2000


def send_empty_message_for_char(c):
    packet = IP(dst='0.0.0.0')/UDP(dport=MOVE_PORT + ord(c))/Raw(load="")
    packet.show()
    send(packet)


def secret_message_client(message):
    for c in message:
        send_empty_message_for_char(c)
