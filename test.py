#Premier programme
print "#Premier programme"
print "Hello World ! "


#Utiliser une variable
var = "Lucie"
print "Je m'apelle "+ var +"!"


#Tuple
myTuple = ("toto","tata", 123)
print myTuple[1]

#Liste
print "#Liste"
myShoppingList = ["Banane", "Poireaux", "Raclette", "Caviar", "Picon"]
print myShoppingList[2]
print len(myShoppingList)

#for in
print "#for in"
for aliment in myShoppingList:
    print aliment

print myShoppingList

#while
print "#while1"
i = 0
while i < len(myShoppingList):
    print myShoppingList[i]
    i = i + 1

#while
print "#while2"
i = 0
while i <= len(myShoppingList) -1:
    print myShoppingList[i]
    i = i + 1

        
#Dictionnaire
user = {
    "Surname": "Prd",
    "Firstname": "Lucie",
    "Age": 22

}
print user
print user["Age"]

#Double tableau
#myList = (User, User1)
#print "Jerome a" + str(myList[1]["Age"])

#Utilisation Append : Ajouter un élement à la fin de la liste
myShoppingList = ["Banane", "Poireaux", "Raclette", "Caviar", "Picon"]
myShoppingList.append("Poires") 
print myShoppingList




