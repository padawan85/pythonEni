from scapy.all import *

def pkt_callback(packet):
	http_packet=str(packet)
	http_test=int(http_packet.find('POST'))
	if http_test != -1:
		Post_print(packet)

def Post_print(packet1):
    res =  "***************************************POST PACKET START**********************************************\n"
    res += "\n".join(packet1.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
    res += "***************************************POST PACKET END************************************************\n"
    print res
print "Waiting for Post packet interception"

sniff(prn=pkt_callback, filter="tcp port 80")
