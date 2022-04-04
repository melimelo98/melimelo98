i = 0
j = 0
nombrecolonne = int(input("nombre de colonne ?\n"))
nombreligne = int(input("nombre de ligne ?\n"))

while j < nombreligne :
	while i < nombrecolonne :
		print("@" , end = '')
		i = i + 1
	print("")
	i = 0
	j = j + 1