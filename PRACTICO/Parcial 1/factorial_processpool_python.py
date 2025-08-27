
# Importa el módulo concurrent.futures para trabajar con procesos
import concurrent.futures
# Importa el módulo math para usar la función factorial
import math
# Importa el módulo time para medir el tiempo de ejecución
import time

# Función que calcula el factorial de un número n
def factorial(n):
    return math.factorial(n)

# Punto de entrada principal del script
if __name__ == "__main__":
    # Crea una lista de números del 1 al 100
    numbers = list(range(1, 101))
    # Guarda el tiempo de inicio
    start = time.time()
    # Crea un ProcessPoolExecutor para ejecutar tareas en procesos independientes (paralelismo real)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Ejecuta la función factorial en paralelo para cada número usando procesos
        results = list(executor.map(factorial, numbers))
    # Guarda el tiempo de finalización
    end = time.time()
    # Imprime los resultados de los factoriales
    for n, f in zip(numbers, results):
        print(f"{n}! = {f}")
    # Imprime el tiempo total de ejecución
    print(f"Tiempo total usando ProcessPoolExecutor: {end - start:.4f} segundos")
