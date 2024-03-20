# Python program to display all the prime numbers within an interval
# Programa de python para mostrar todos los numeros primos dentro de un intervalo

# Limits of the interval
# Limites del intervalo
inferior = 1
superior = 100

print("Los numeros primos entre", inferior, "y", superior, "son:")

# Iterate through all numbers of the interval
# Itera a traves de todos los numeros del intervalo

for num in range(inferior, superior + 1):
    # Todos lo numeros primos son mas grandes que  1
    if num > 1:

        # Revisa si el numero es diviisble por algun numero menor asi mismo
        for i in range(2, num):
            if (num % i) == 0: #Si es divisible no es primo
                break
        else:  # Si no es divisible es primo
            print(num)

