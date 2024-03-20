import matplotlib.pyplot as plt

def collatz_secuencia(num):
    secuencia = [num]
    while num !=1:
        if num % 2 == 0:
            num=num //2
        else:
            num=3*num+1
        secuencia.append(num)
    return secuencia

def iteracion_collatz(num):
    iteraciones = 0
    while num != 1:
        if num % 2 ==0:
            num = num // 2
        else:
            num = 3 * num + 1
        iteraciones += 1
    return iteraciones


# Calcular la secuencia de Collatz y el número de iteraciones para cada número en el rango
num_valores = range(1, 10001)
iteraciones_valores = [iteracion_collatz(num) for num in num_valores]

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(iteraciones_valores, num_valores, marker=".", color="blue")
plt.title("Secuencia de Collatz")
plt.xlabel("Número de iteraciones")
plt.ylabel("Número inicial (n)")
plt.grid(True)
plt.show()
