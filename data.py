bin_valid_chars = ["0","1"]
dec_valid_chars = bin_valid_chars + ["2","3","4","5","6","7","8","9"]
hex_valid_chars = dec_valid_chars + ["A","B","C","D","E","F","a","b","c","d","e","f"]
valid_base = ["2","10","16"]

ask_for_the_init_number_text = "donne moi le nombre : "
ask_again_for_the_init_number_text = "c'est incorecte donne moi encore le nombre : "

ask_for_the_init_base_text = "donne moi la base de départ"
ask_for_the_target_base_text = "donne moi la base d'arrivé"

ask_for_the_init_base_text = "donne moi la base de départ:"
ask_for_the_target_base_text = "donne moi la base d'arrivé:"


def decimal_to_binary(decimal_number):
    return bin(decimal_number).replace("0b", "")
number = int(input("Entrez un nombre décimal : "))
binary_number = decimal_to_binary(number)
print(f"Le nombre binaire de {number} est : {binary_number}")


def binaire_vers_decimal(nombre_binaire):
    decimal = int(nombre_binaire, 2)
    return decimal
print(f"Le nombre binaire est {decimal}")

