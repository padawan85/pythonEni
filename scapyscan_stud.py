from scapy.all import *
import sys
import os
from colorama import Fore,Style
import math

def scanport(ipaddressdst,firstport,lastport):
    lastport+=1
    numop=0
    for i in range(firstport,lastport):
        numop += hiu(ipaddressdst,i)
    return numop
        

def hiu(d,port):
    conf.verb = 0
    a = IP()
    b = TCP()
    a.dst = d
    b.dport = port
    b.flags = 'S'
    tcpport = a/b
    SYN = 0x02
    ACK = 0x10
    SYNACK = SYN | ACK
    res = sr1(tcpport)
    i = 0
    if res['TCP'].flags == SYNACK:
        print Fore.GREEN+"Connection on the port: ",port,"\t\t Port Open"
        print(Style.RESET_ALL)
        i += 1
        
    else:
        print Fore.RED+"Couldnt connect on the port ",port,"\t Port Close"
        print(Style.RESET_ALL)
    
    return(i)
    
def main():
    os.system('cls')
    print """

       /$$   /$$ /$$      /$$  /$$$$$$  /$$$$$$$        /$$$$$$$  /$$   /$$       /$$$$$$$   /$$$$$$  /$$   /$$ /$$    /$$ /$$$$$$$  /$$$$$$$$      
      | $$$ | $$| $$$    /$$$ /$$__  $$| $$__  $$      | $$__  $$| $$  | $$      | $$__  $$ /$$__  $$| $$  | $$| $$   | $$| $$__  $$| $$_____/      
      | $$$$| $$| $$$$  /$$$$| $$  \ $$| $$  \ $$      | $$  \ $$| $$  | $$      | $$  \ $$| $$  \ $$| $$  | $$| $$   | $$| $$  \ $$| $$            
      | $$ $$ $$| $$ $$/$$ $$| $$$$$$$$| $$$$$$$/      | $$  | $$| $$  | $$      | $$$$$$$/| $$$$$$$$| $$  | $$|  $$ / $$/| $$$$$$$/| $$$$$         
      | $$  $$$$| $$  $$$| $$| $$__  $$| $$____/       | $$  | $$| $$  | $$      | $$____/ | $$__  $$| $$  | $$ \  $$ $$/ | $$__  $$| $$__/         
      | $$\  $$$| $$\  $ | $$| $$  | $$| $$            | $$  | $$| $$  | $$      | $$      | $$  | $$| $$  | $$  \  $$$/  | $$  \ $$| $$            
      | $$ \  $$| $$ \/  | $$| $$  | $$| $$            | $$$$$$$/|  $$$$$$/      | $$      | $$  | $$|  $$$$$$/   \  $/   | $$  | $$| $$$$$$$$      
      |__/  \__/|__/     |__/|__/  |__/|__/            |_______/  \______/       |__/      |__/  |__/ \______/     \_/    |__/  |__/|________/      
                                                                                                                                                    
                                                                                                                                                    
                                                                                                                                                    
              /$$$$$$  /$$    /$$ /$$$$$$$$  /$$$$$$         /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$  /$$     /$$                                     
             /$$__  $$| $$   | $$| $$_____/ /$$__  $$       /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$|  $$   /$$/                                     
            | $$  \ $$| $$   | $$| $$      | $$  \__/      | $$  \__/| $$  \__/| $$  \ $$| $$  \ $$ \  $$ /$$/                                      
            | $$$$$$$$|  $$ / $$/| $$$$$   | $$            |  $$$$$$ | $$      | $$$$$$$$| $$$$$$$/  \  $$$$/                                       
            | $$__  $$ \  $$ $$/ | $$__/   | $$             \____  $$| $$      | $$__  $$| $$____/    \  $$/                                        
            | $$  | $$  \  $$$/  | $$      | $$    $$       /$$  \ $$| $$    $$| $$  | $$| $$          | $$                                         
            | $$  | $$   \  $/   | $$$$$$$$|  $$$$$$/      |  $$$$$$/|  $$$$$$/| $$  | $$| $$          | $$                                         
            |__/  |__/    \_/    |________/ \______/        \______/  \______/ |__/  |__/|__/          |__/                                         
                                                                                                                                                    
                                                                                                                                                    
                                                                                                                                                    
                                     /$$$$$$$  /$$     /$$       /$$$$$$$$  /$$$$$$                                                                 
                                    | $$__  $$|  $$   /$$/      | $$_____/ /$$__  $$                                                                
                                    | $$  \ $$ \  $$ /$$/       | $$      | $$  \ $$                                                                
                                    | $$$$$$$   \  $$$$/        | $$$$$   | $$$$$$$$                                                                
                                    | $$__  $$   \  $$/         | $$__/   | $$__  $$                                                                
                                    | $$  \ $$    | $$          | $$      | $$  | $$                                                                
                                    | $$$$$$$/    | $$          | $$$$$$$$| $$  | $$                                                                
                                    |_______/     |__/          |________/|__/  |__/                                                                

                                            Un mini nmap du pauvre avec SCAPY
    """
    
    hostdst= raw_input("What is the host scanned : ")
    firstPort = raw_input("What is the first port scanned : ")
    lastPort = raw_input("What is the first port scanned : ")
    print ("\n")
    try:
        firstPort=int(firstPort)
        lastPort=int(lastPort)
    except:
        print "Impossible de convertir les variables"
    start = time.time()
    print scanport(hostdst,firstPort,lastPort),"ports d'ouvert"
    end = time.time()
    print "Le script dure: ", round(end - start,2),"secondes"
    
main()
