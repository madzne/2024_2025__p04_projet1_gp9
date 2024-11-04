from fonctions import*

nombre = (input("entrez un nombre :\n"))
base = input("c'est quelle base : (b or d or h):\n")

print (nombre)

while not (verifie_base_et_nombre(nombre, base)):
    print("votre saisi n'est pas valide")
    nombre = input("entrez un nombre ::\n")
    base = input("c'est quelle base ::\n")

futur_base = input("entrez la base souhaitée :\n")

while not (verifie_futur_base(futur_base)):
    print ("faux")
    futur_base = input("entrez la base souhaitée:\n")

if base == "b" and futur_base == "d":
    nouveau_nombre = binaire_vers_decimal(nombre)
    
elif base == "d" and futur_base == "h":
    nouveau_nombre = decimal_vers_hexadecimal(nombre)
    
elif base == "b" and futur_base == "h":
    nouveau_nombre = binaire_vers_hexadecimal(nombre)
    
elif base == "d" and futur_base == "b":
    nouveau_nombre = decimal_vers_binaire(nombre)

elif base == "h" and futur_base == "b":
    nouveau_nombre = hexadecimal_vers_binaire(nombre)

elif base == "h" and futur_base == "d":
    nouveau_nombre = hexadecimal_vers_decimal(nombre)

elif base == "d" and futur_base == "d":
    nouveau_nombre = nombre

elif base == "b" and futur_base == "b":
    nouveau_nombre = nombre

elif base == "h" and futur_base == "h":
    nouveau_nombre = nombre
        
print ("le nouveau nombre est", nouveau_nombre)




