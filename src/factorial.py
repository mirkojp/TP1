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

#Revisar si el argumento no esta vacio
if len(sys.argv) == 0:
   print("Debe informar un número!")
   sys.exit()

#Convertir argumento en numero entero
num=int(sys.argv[1])

#Imprimimos el resultados
print("Factorial ",num,"! es ", factorial(num)) 
