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



# Verificar si se proporciona un argumento en la línea de comandos
if len(sys.argv) == 1:
    # Si no se proporciona un argumento, solicitar al usuario que ingrese el número
    while True:
        try:
            num = int(input("Ingrese un número para calcular su factorial: "))
            break
        except ValueError:
            print("Debe ingresar un número válido.")

else:
    num = int(sys.argv[1])


# Calcular y mostrar el factorial
if num is not None:
    print("Factorial", num, "! es", factorial(num))
