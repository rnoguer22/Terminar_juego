import random
MIN = 0
MAX = 99
numero_bueno = random.randint(MIN,MAX)

def pedir_numero (minimo=MIN, maximo=MAX):
    while True:
        entrada = int (input ("Introduce un numero entre " + str(minimo) + " y " + str(maximo) + " :"))
        if  minimo <= entrada <= maximo:
            break
    return entrada

minimo = MIN
maximo = MAX
print ("Comienza el juego, adivina el numero aleatorio")

while True: 
    intento = pedir_numero(minimo, maximo)
    if intento < numero_bueno:
        print("Demasiado pequeño")
    elif intento > numero_bueno:
        print ("Demasiado grande")
    else:
        print ("¡Ha ganado!")
        break