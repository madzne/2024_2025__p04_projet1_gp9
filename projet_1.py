from tools import *
from data import *

# faire les nombres de bin to exa et inversement en passant par bin to dec puis dec to exa et inversement
def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    pass
    target_number = None
    return target_number


# assert bin_dec_hex__to__bin_dec_hex ("101", 2, 10) == "5"

ask_for_the_init_number_text = "Le nombre ? :"

ask_again_for_the_init_number_text = "Le nombre put*** ! : "

bin_number_valid_chars = ["0", "1"]

dec_number_valid_chars = \
    bin_number_valid_chars \
  + ["2", "3", "4", "5", "6", "7", "8", "9"]

hex_number_valid_chars = \
    dec_number_valid_chars \
  + ["A", "B", "C", "D", "E", "F"] \
  + ["a", "b", "c", "d", "e", "f"]

def check_char_number_validity (char):
    return char in hex_number_valid_chars

def is_a_valid_number (number):
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i <= len (number) - 1:
        is_a_valid_char = check_char_number_validity (number [i])
        i = i + 1
    return is_a_valid_char

def ask_for_the_init_number ():
    init_number = input (ask_for_the_init_number_text)
    while not (is_a_valid_number (init_number)) == True:
        init_number = input (ask_again_for_the_init_number_text)
    return init_number
        

def is_a_valid_base (n):
    return n in valid_base 
    

def is_a_valid_base(number):
    number == valid_base
    while number not in valid_base:
        number = False
        input(ask_again_for_the_base)
    return number


# regler le probleme dans la console parce que demande le mauvais truc

    


def ask_for_the_init_base ():
    init_base = input(ask_for_the_init_base_text)
    while not (is_a_valid_base(init_base)) == True:
        init_base = input(re_ask_for_the_init_base_text)
    return init_base


    

        



    

def ask_for_the_target_base():
    target_base= input(ask_for_the_target_base_text)
    while not(is_a_valid_base(target_base)) == True:
        target_base = input(re_ask_for_the_target_base_text)
        return target_base





def do_the_job ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = \
      bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base)
    
do_the_job()



# def decimal_to_bin (n, d):
#     q = n // d 
#     restes = ""
#     while q > 0 :

#         reste = n % 2
#         n = q
#         q = n // 2
#         restes= reste + restes
#         return restes

# def dec_to_bin (n, d):
#     q = n // d 
#     restes = ""
#     while q > 0 :

#         restes = n % 2
#         n = q
#         q = n // 2
#         restes = restes + restes

def decimal_to_bin(n):
    if n == 0:
        return "0"
    restes = ""
    while n > 0:
        reste = n % 2  # Trouver le reste (0 ou 1)
        restes = str(reste) + restes  # Ajouter le reste au début de la chaîne
        n = n // 2  # Mettre à jour le quotient
    return restes

# Exemple d'utilisation
nombre_decimal = 13
print(f"Le binaire correspondant à {nombre_decimal} est {decimal_to_bin(nombre_decimal)}")


