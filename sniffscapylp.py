from scapy.all import *
import time

print "Attente de requete"
time.sleep(2)

def scapy_callback(packet):
    http_packet=str(packet)
    if int(http_packet.find('POST')):
        return POST_print(packet)
    
    
def POST_print(pkt):
    ret = "***************************************POST PACKET****************************************************\n"
    ret += "\n".join(pkt.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
    ret += "*****************************************************************************************************\n"
    return ret
    

sniff(prn=scapy_callback, lfilter=lambda p: "POST" in str(p), filter="tcp port 80")



