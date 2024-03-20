# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * calcula el factorial de un número                                       *
# * Dr.P.E.Colla (c) 2022                                                   *
# * Creative commons                                                        *
# *-------------------------------------------------------------------------*
import sys

# Funcion para calcular el factorial de un numero
def factorial(num): 
    # Manejo de caso de numeros negativos
    if num < 0: 
        print("Factorial de un número negativo no existe")

    # Manejo de caso de 0
    elif num == 0:
        return 1

    # Manejo de caso numero enteros positivos
    else: 
        fact = 1
        # Iteracion calculo factorial
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Funcion para calcular el factorial entre un limite inferior y superior
def factorial_rango(desde,hasta):

    # Lista guarda las valores
    factoriales = []

    # Itera por todos los valores del intervalo
    for num in range(desde,hasta+1):
        #Llama a funcion factorial
        fact = factorial(num)
        #Si existe lo guarda
        if fact is not None:
            factoriales.append((num, fact))

    return factoriales



# Verificar si se proporciona un argumento en la línea de comandos
if len(sys.argv) == 1:
    # Si no se proporciona un argumento, solicitar al usuario que ingrese el rango
    while True:
        try:
            rango = input("Ingrese un rango (desde-hasta) para calcular los factoriales: ")

            #Caso -hasta
            if rango.startswith("-"):
                desde = 1
                hasta = int(rango.split("-")[1])
                break
            #Caso desde-
            elif rango.endswith("-"):
                desde = int(rango.split("-")[0])
                hasta = 60
                break
            #Caso desde-hasta
            if "-" in rango:
                desde, hasta = map(int, rango.split("-"))
                break
            else:
            #levantar error
                raise ValueError
        except ValueError:
            print("Debe ingresar un rango válido en el formato 'desde-hasta', '-hasta' o 'desde-'.")

else:
    # Si se proporciona un argumento en la línea de comandos, lo interpreta como un rango automáticamente
    rango = sys.argv[1]

    #Caso -hasta
    if rango.startswith("-"):
        desde = 1
        hasta = int(rango.split("-")[1])
    #Caso desde-
    elif rango.endswith("-"):
        desde = int(rango.split("-")[0])
        hasta = 60
    #Caso desde-hasta
    elif "-" in rango:
        desde, hasta = map(int, rango.split("-"))

# Calcular los factoriales en el rango especificado
factoriales = factorial_rango(desde, hasta)

# Mostrar los resultados
if factoriales:
    print("Los factoriales en el rango", desde, "-", hasta, "son:")
    #Itera por todos los valores
    for num, fact in factoriales:
        print("Factorial de", num, "es", fact)
else:
    print("No se encontraron factoriales en el rango especificado.")
