MIN = 0
MAX = 99

def pedir_numero ():
    while True:
        entrada = input ("Introduce un numero entre ", MIN, " y ", MAX, " :")
        try:
            int (entrada)
        except:
            pass
        else: 
            if 0 <= entrada <= 99:
                break
        return entrada