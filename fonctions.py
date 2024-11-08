from data import*

#base (str) et nombre (str) donnés par l'utilisateur 
#d'abord on verifie que la base est une des trois possibilitées puis on verifie que les charactèere du nombres appaartiennent bien a la bases
#retourne un Bolleen (True or False) 
def verifie_base_et_nombre(number,base):
    if not verifie_futur_base(base):
        return False
    
    if base == "d":
        for elem in number :
            if not elem in dec_valid_chars :
                return False
    
    elif base == "b":
        for elem in number :
            if not elem in bin_valid_chars:
                return False
    
    elif base == "h":
        for elem in number:
            if not elem in hex_valid_chars :
                return False 
    return True 

#base demandé par l'utilisateur (str)
#verifie que la base est une des trois bases possibles
#retourne un Bolleen (True or False)
def verifie_futur_base(futur_base):
    if futur_base == "h" or  futur_base == "d" or futur_base == "b":
        return True
    else:
        return False 

#nombre (str)
#retourne le nouveau nombre (str)
def binaire_vers_decimal(nombre) :
    resultat_avant = 0
    for i in range (len(nombre),0,-1):
        nouveau_nombre = (2**(len(nombre)-i))*int(nombre[i-1])
        resultat_avant = resultat_avant + nouveau_nombre
    return resultat_avant

#nombre (str)
#retourne le nouveau nombre (str)
def decimal_vers_hexadecimal(nombre):
    nombre = int(nombre)
    nouveau_nombre = ""
    while nombre != 0 :
        if nombre % 16 == 10:
           reste = "A"
        elif nombre % 16 == 11 :
            reste = "B"
        elif nombre % 16 == 12:
            reste = "C"
        elif nombre % 16 == 13 :
            reste = "D"
        elif nombre % 16 == 14 :
            reste = "E"
        elif nombre % 16 ==  15 :
            reste ="F"
        else :
            reste = nombre % 16
        nouveau_nombre = nouveau_nombre  + str(reste)
        nombre = nombre // 16
    nouveau_nombre = nouveau_nombre[::-1]    #chatgpt
    
    return nouveau_nombre

#nombre (str)
#retourne le nouveau nombre (str)
def binaire_vers_hexadecimal(nombre):
    quatior = ""
    somme_des_nombres = ""
    while len(nombre) % 4 != 0 :
        nombre =  "0" + nombre
    
    for i in range (0, len(nombre),4):
        quatior = binaire_vers_decimal(nombre[i:i+4])
        quatior = decimal_vers_hexadecimal(quatior)
        somme_des_nombres = somme_des_nombres + quatior
    return somme_des_nombres
        
#nombre (str)
#retourne le nouveau nombre (str)
def decimal_vers_binaire(nombre):
    nombre = int(nombre)
    nouveau_nombre = ""
    while nombre != 0 :
        nouveau_nombre = nouveau_nombre  + str(nombre % 2)
        nombre = nombre // 2
    nouveau_nombre = nouveau_nombre[::-1]    #chatgpt
    return nouveau_nombre

#nombre (str)
#retourne le nouveau nombre (str)
def hexadecimal_vers_binaire(nombre):
    resultat = decimal_vers_binaire(hexadecimal_vers_decimal(nombre))
    for elem in nombre[1:]:
        # resultat = resultat + hexadecimal_vers_decimal(decimal_vers_binaire(elem))
        # resultat = resultat + decimal_vers_binaire(hexadecimal_vers_decimal(elem))
        nb = hexadecimal_vers_decimal(elem)
        #print  ("result",resultat)
        #print("elem:",elem)
        #print("fct",decimal_vers_binaire_quatre_bit(nb))
        #resultat += decimal_vers_binaire_quatre_bit(nb)
        
    return resultat



# def decimal_vers_binaire_quatre_bit(nb):
#     if int(nb) >= 8:
#         resultat = ""
#     elif int(nb) >= 4:
#         resultat = "0"
#     elif int(nb) >= 2:
#         resultat = "00"
#     else:
#         if int(nb) == 0:
#             return "0000"
#         else:
#             return "0001"
#     #print ("nb =",nb,"result = ",resultat,"fct = ",decimal_vers_binaire(nb))
#     return resultat+decimal_vers_binaire(nb)

#nombre (str)
#retourne le nouveau nombre (str)
def hexadecimal_vers_decimal(nombre):
    resultat_avant = 0
    for i in range (len(nombre),0,-1):
        if nombre[i-1] == "A" or nombre[i-1] == "a":
            lettre = 10
        elif nombre[i-1] == "B" or nombre[i-1] == "b":
            lettre = 11
        elif nombre[i-1] == "C" or nombre[i-1] == "c":
            lettre = 12
        elif nombre[i-1] == "D" or nombre[i-1] == "d":
            lettre = 13
        elif nombre[i-1] == "E" or nombre[i-1] == "e":
            lettre = 14
        elif nombre[i-1] == "F" or nombre[i-1] == "f":
            lettre = 15
        else :
            lettre = nombre[i-1]
            
        nouveau_nombre = (16**(len(nombre)-i))*int(lettre)
        resultat_avant = resultat_avant + nouveau_nombre
    return str(resultat_avant)

#print(decimal_vers_binaire("6"))
#print(hexadecimal_vers_binaire("7"))

