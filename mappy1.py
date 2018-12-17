print """
----------------------------------------------------------                                                 
,--.   ,--.  ,---.  ,------. ,------.,--.   ,--. 
|   `.'   | /  O  \ |  .--. '|  .--. '\  `.'  /  
|  |'.'|  ||  .-.  ||  '--' ||  '--' | '.    /   
|  |   |  ||  | |  ||  | --' |  | --'    |  |    
`--'   `--'`--' `--'`--'     `--'        `--'    
                                                 
	Author : Lucie P
	Date : 17/12/18
	Description : Scan de ports
----------------------------------------------------------

"""

import socket
import time

#Déclaration des variables
ip = raw_input("Entrer une adresse IP: ") 
portmin = int(raw_input("Entrer un port min: "))
portmax = int(raw_input("Entrer un port max : ")) +1
port = 0

#Dictionnaire Port / services
services = {21:"FTP", 22:"SSH", 23:"Telnet", 25:"SMTP", 80:"HTTP", 53:"DNS"}

#test de l'ouverture du port
def isOpen(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
                s.connect((ip, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
                return False
        finally:
                s.close()

start_time = time.time()
#boucle test de port + impression à l'écran
while port < portmax:
    for i in range(portmin, portmax):
        port = i
        if isOpen(ip, port):
                print "Port : " + str(port) + " opened " + services.get(port)
        else:
                print "Port : " + str(port) + " closed"
                
    print "\n-------------------------------------------------"
    print "Temps d'execution : %s secondes ---" % (time.time() - start_time)
    print "-------------------------------------------------"
    break
