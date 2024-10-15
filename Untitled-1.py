
def decimal_to_bin (n, d):
    q = n // d 
    restes = ""
    while q > 0 :

        reste = n % 2
        n = q
        q = n // 2
        restes= reste + restes
        return restes
