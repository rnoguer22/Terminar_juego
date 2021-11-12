import random
MIN = 0
MAX = 99
numero_bueno = random.randint(MIN,MAX)

def pedir_numero ():
    while True:
        entrada = int (input ("Introduce un numero entre " + str(MIN) + " y " + str(MAX) + " :"))
        if MIN <= entrada <= MAX:
            break
    return entrada

print ("Comienza el juego, adivina el numero aleatorio")

while True: 
    intento = pedir_numero()
    if intento < numero_bueno:
        print("Demasiado pequeño")
    elif intento > numero_bueno:
        print ("Demasiado grande")
    else:
        print ("¡Ha ganado!")
        break