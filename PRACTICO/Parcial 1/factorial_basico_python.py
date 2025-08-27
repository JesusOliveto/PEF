
import time

# Calcula el factorial de un número n de forma básica (sin usar math.factorial)
def factorial_basico(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

if __name__ == "__main__":
    # Crea una lista de números del 1 al 100
    numbers = list(range(1, 101))
    # Guarda el tiempo de inicio
    start = time.time()
    # Calcula el factorial de cada número de forma secuencial
    resultados = [factorial_basico(n) for n in numbers]
    # Guarda el tiempo de finalización
    end = time.time()
    # Imprime los resultados de los factoriales
    for n, f in zip(numbers, resultados):
        print(f"{n}! = {f}")
    # Imprime el tiempo total de ejecución
    print(f"Tiempo total usando método básico: {end - start:.4f} segundos")
