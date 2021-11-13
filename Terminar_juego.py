import random
MIN = 0
MAX = 0

while True:
    nivel = input ("Seleccione un nivel, simple, intermedio, avanzado, o experto: ")
    try:
        if nivel == "simple":
            MAX = 100
            break
        elif nivel == "intermedio":
            MAX = 1000
            break
        elif nivel == "avanzado":
            MAX = 1000000
            break
        elif nivel == "experto":
            MAX = 1000000000000
            break
    except:
        pass

def pedir_numero (minimo=MIN, maximo=MAX):
    while True:
        entrada = int (input ("Introduce un numero entre " + str(minimo) + " y " + str(maximo) + " : "))
        if  minimo <= entrada <= maximo:
            break
    return entrada

numero_bueno = random.randint(MIN,MAX)
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