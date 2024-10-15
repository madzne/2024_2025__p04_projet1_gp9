def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    pass
    target_number = None
    return target_number

from tools import *
from data import *

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
        
def is_a_valid_base(n):
    n == valid_base
    while n not in valid_base:
        n = False
        input(ask_again_for_the_base)
    return good_answer

# regler le probleme dans la console parce que demande le mauvais truc

    


def ask_for_the_init_base ():
    init_base = input(ask_for_the_init_base_text)
    while not (is_a_valid_base(init_base)) == True:
        init_base = input(ask_for_the_init_base_text)
    return init_base


    

        



    

def ask_for_the_target_base():
    target_base= input(ask_for_the_target_base_text)





def do_the_job ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = \
      bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base)
    
do_the_job()















def decimal_to_bin (n, d):
    q = n // d 
    restes = ""
    while q > 0 :

        reste = n % 2
        n = q
        q = n // 2
        restes= reste + restes
        return restes






    