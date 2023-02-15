from scapy.all import *
from scapy.layers.dns import *


def filter_dns(pack):
    if UDP in pack:
        return 2000 <= pack[UDP].dport <= 2500 and 'RAW' not in pack
    return False


capture = sniff(lfilter=filter_dns, prn=lambda x: print(chr(x[UDP].dport-2000), end=""))
