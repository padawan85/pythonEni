# -*- coding: cp1252 -*-

import time
from scapy.all import *

#Declaration des variables
ipd = str(raw_input("Entrer une adresse IP: ")) 
portmin = str(raw_input("Entrer un port min: "))
portmax = str(raw_input("Entrer un port max : "))
ports = RandShort()
port = 0
ips = "10.101.200.13"

#Dictionnaire Port / services
services = {21:"FTP", 22:"SSH", 23:"Telnet", 25:"SMTP", 80:"HTTP", 53:"DNS"}


def isPortUp(ips,ipd,portmin, portmax):
# SYN
    ip=IP(src=ips,dst=ipd)
    SYN=TCP(sport=ports,dport=port,flags='S',seq=1000)
    SYNACK=sr1(ip/SYN)

# ACK
    ACK=TCP(sport=ports, dport=port, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + 1)
    send(ip/ACK)


# Selon le résultat du flags, on affiche "ouvert" ou "fermé"
    for port in range(portmin, portmax):
            if ACK.flags == 'A':
                    print "Port : " %port + " opened " + services.get(port)
            else:
                    print "Port : " + str(port) + " closed"

isPortUp(ips,ipd,portmin,portmax)

start_time = time.time()
#boucle test de port + impression à l'écran
               
print "\n-------------------------------------------------"
print "Temps d'execution : %s secondes ---" % (time.time() - start_time)
print "-------------------------------------------------"

