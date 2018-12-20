import base64, binascii, os, string, random, requests, webbrowser
import subprocess as sp
from cryptography.fernet import Fernet


tag = ".P2CIGEFQ"
key = "Do6pFr65O0s-Ff-kgf-UGvlYdgA4rjzUApTCz981dZI="
home = os.getenv('HOME')




for root, dirs, files in os.walk(home):
    for file in files:
        if file.endswith(str(tag)):
            listedfile =(os.path.join(root, file))
            print listedfile 
            fichier = open(listedfile, "r")
            content = fichier.read()

            f = Fernet(key)
            fernetdecry = f.decrypt(content)
            #unhexfi = (binascii.unhexlify(fernetdecry))
            fichier.close()

            fichier = open(str(listedfile) + ".resc2", "ab")
            fichier.write(fernetdecry )
            fichier.close()

            os.remove(str(listedfile))
