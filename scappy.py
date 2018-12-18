from scapy.all import *

def isHostUp(d,s):
    a = IP()
    b = ICMP()

    a.dst = d
    a.src = s

    ping = a/b
    res = sr1(ping)

if res.code = 0:
    return True
else:
    return False

print isHostUp("10.101.200.28","10.101.200.13")
