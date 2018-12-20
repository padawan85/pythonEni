#Recuperer le contenu du presse-papiers et l envoyer faire le serveur web


import clipboard, webbrowser, requests, base64

#variables
web = 'http://10.101.200.38/index.php?args='


url = clipboard.paste()

if url != '':
	urlencode = url.encode('base64')
	requests.get(web + urlencode)


#	webbrowser.open(web + url)




