#Recuperer le contenu du presse-papiers et l envoyer faire le serveur web


import clipboard, webbrowser, requests

#variables
web = 'http://10.101.200.38/index.php?args='


url = clipboard.paste()
clipboard.copy(url)

#requests.get(web + url)



webbrowser.open(web + url)


