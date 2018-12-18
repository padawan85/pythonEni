import os, socket, math, time
from colorama import Fore, Back, Style


def main():
    # TO CLEAR
    os.system('cls')
    # NAME OF THE SCRIPT
    print """
 ____   ____    _    _   _ ____  ____   ___  ____ _____ 
/ ___| / ___|  / \  | \ | |___ \|  _ \ / _ \|  _ \_   _|
\___ \| |     / _ \ |  \| | __) | |_) | | | | |_) || |  
 ___) | |___ / ___ \| |\  |/ __/|  __/| |_| |  _ < | |  
|____/ \____/_/   \_\_| \_|_____|_|    \___/|_| \_\|_|  

                                                By Ben

"""
    
# CALLING MAIN DEF
main()

# QUESTIONS FOR THE USER
ipHote=str(raw_input("Tape l'IP de la machine que tu veux scanner: "))
minPort= int(raw_input("Tape le Port de depart: "))
maxPort= int(raw_input("Tape le Port de fin: "))

#TRY TRY AND RETRY WHITHOUT ANY QUESTION
"""
ipHote="10.101.200.28"
minPort=20
maxPort=30
"""

# VAR TO COUNT NB OF OPEN PORTS
nbPortOpen = int(0)

#TO MAKE IT BEAUTYFULL
print "\n"
print "------------------------"

maxPort += 1
t1 = time.time()

# SOCKET SHITS TO TRY EVERY PORTS
for ports in range(minPort, maxPort):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result=s.connect_ex((ipHote, ports))
    if result == 0 :
        #WHAT WILL BE PRINT IF PORT OPEN
        print  "[+] Port {} est".format(ports)+ Fore.GREEN + " OPEN" + Fore.WHITE
        nbPortOpen += 1
    else:
        #WHAT WILL BE PRINT IF PORT CLOSE
        print "[-] Port {} est".format(ports) + Fore.RED +" CLOSE" + Fore.WHITE
    s.close()

t2 = time.time()
t3 = round(t2-t1, 2)

#TO MAKE IT BEAUTYFULL
print "------------------------"    

#PRINT THE NUMBER OF OPEN PORTS
print "\nIl y a "+ str(nbPortOpen)+ " port(s)"+ Fore.GREEN + " OPEN" + Fore.WHITE +". La recherche aura pris " + str(t3) + " secondes" #CHEAT ON TIME

