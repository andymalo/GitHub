#Ouverture du fichier
#si file n'existe pas
#	créer un file
#écrire à la suite séparé à un saut de ligne

file = open("exemple.txt","w")

lst = ["Line 1","Line 2","Line 3", "Line 4","Line 5","Line 6"]

for i in lst:
	file.write(i + "\n")

file.close()

file = open("exemple.txt","r")
file.seek(0)
content = file.read()

print(content)