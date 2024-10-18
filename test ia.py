from data import*
def hex_to_decimal(hex_num):
    decimal = 0
    hex_num = hex_num.upper()  # Pour uniformiser les majuscules et minuscules

    # Liste des caractères hexadécimaux valides et leurs valeurs en décimal
    hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hex_values = {hex_chars[i]: i for i in range(len(hex_chars))}

    # Inverser la chaîne hexadécimale pour traiter de droite à gauche
    hex_num = hex_num[::-1]

    # Boucler à travers chaque caractère du nombre hexadécimal
    for i in range(len(hex_num)):
        char = hex_num[i]  # Obtenir le caractère de la position i
        if char in hex_valid_chars:
            value = hex_values[char]  # Obtenir la valeur décimale du caractère hexadécimal
        else:
            raise ValueError("Caractère non valide dans le nombre hexadécimal")

        # Ajouter la valeur correspondante à la somme totale, en prenant en compte la puissance de 16
        decimal += value * (16 ** i)

    return decimal

# Entrer un nombre hexadécimal
hex_number = input("Entrez un nombre hexadécimal : ")

# Conversion et affichage du résultat
print (f"Le nombre décimal est :", hex_to_decimal(hex_number))