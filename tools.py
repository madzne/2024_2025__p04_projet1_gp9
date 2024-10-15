bin_valid_chars=["0","1"]
dec_valid_chars= bin_valid_chars +["2","3","4","5","6","7","8","9"]
hex_valid_chars= dec_valid_chars +["A","B","C","D","E","F","a","b","c","d","e","f"]

def is_a_valid_base(n):
    while n not in valid_base:
        n = False
        input(ask_again_for_the_base)
    return 