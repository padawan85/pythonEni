import sys, base64

arg = sys.argv[1].decode('base64')
fichier = open("fic.log", "a")

fichier.write(arg)
fichier.write("\n")
