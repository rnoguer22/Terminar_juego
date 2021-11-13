import random
MIN = 0
MAX = 0
intentos_max = 0

while True:
    nivel = input ("Seleccione un nivel, simple, intermedio, avanzado, o experto: ")
    try:
        if nivel == "simple":
            MAX = 100
            intentos_max = 10
            break
        elif nivel == "intermedio":
            MAX = 1000
            intentos_max = 20
            break
        elif nivel == "avanzado":
            MAX = 1000000
            intentos_max = 50
            break
        elif nivel == "experto":
            MAX = 1000000000000
            intentos_max = 100
            break
    except:
        pass

def pedir_numero (minimo=MIN, maximo=MAX):
    while True:
        entrada = input ("Introduce un numero: ")
        try:
            entrada = int (entrada)
        except:
            pass
        if  minimo <= entrada <= maximo:
            break
        else:
            print ("Ha introducido un numero que no esta dentro del rango de numeros del juego,"
                "repita por favor")
    return entrada

def ayuda():
    ayudita = input ("Quiere recibir una pequeña ayudita? si o no? ")
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
print ("Tienes " + str(intentos_max) + " intentos, dale a tope!!!")

contador = 0

while contador < intentos_max: 
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

if contador == intentos_max:
    print ("Has alcanzado el numero maximo de intentos, has perdido, paquete...")