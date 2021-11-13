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
        entrada = input ("Introduce un numero: ")
        try:
            entrada = int (entrada)
            if  minimo <= entrada <= maximo:
                break
            else:
                print ("Ha introducido un numero que no esta dentro del rango de numeros del juego,"
                "repita por favor")
        except:
            pass
    return entrada

def ayuda():
    ayudita = input (print ("Quiere recibir una pequeña ayudita? si o no? "))
    if ayudita == "si":
        print ("El numero esta comprendido entre " + str(MIN) + " y " + str(MAX))
    else:
        print ("Como quieras...")
    return ayudita

numero_bueno = random.randint(MIN,MAX)
minimo = MIN
maximo = MAX
hola = ayuda()
print ("Comienza el juego, adivina el numero aleatorio")

contador = 1

while True: 
    intento = pedir_numero(minimo, maximo)
    if intento < numero_bueno:
        contador += 1
        print("Demasiado pequeño")
    elif intento > numero_bueno:
        contador += 1
        print ("Demasiado grande")
    else:
        print ("¡Ha ganado!")
        contador += 1
        print ("Ha necesitado ", contador, " intentos para conseguirlo")
        break