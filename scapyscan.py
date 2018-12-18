import time
from scapy.all import *

conf.verb = 0
ip = raw_input("Target addr >>")

def isTargetUp(ip):
    icmp = IP(dst=ip) / ICMP()
    resp = sr1(icmp, timeout=10)
    if resp == None:
        return False
    else:
        return True


pMin = int(raw_input("Port min: "))
pMax = int(raw_input("Port max: ")) + 1

t1 = time.time()

if isTargetUp(ip):

    print "Host %s is up, start scanning" % ip

    for port in range(pMin, pMax):

        srcPort = RandShort()
        synPacket = IP(dst=ip) / TCP(sport=srcPort, dport=port, flags='S')
        resp = sr1(synPacket, timeout=2)

        if resp:
            if resp.haslayer(TCP):
                if resp.getlayer(TCP).flags == 0x12:
                    send_rst = sr(IP(dst=ip) / TCP(sport=srcPort, dport=port, flags='AR'), timeout=1)
                    print("[+] Port %s is open" % port)
                else: 
                    print("[-] Port %s is closed" % port)
        else:
            print("[-] Port %s is closed" % port)

    totalTime = time.time() - t1
    print("%s Scan Completed in %fs" % (ip, totalTime))
