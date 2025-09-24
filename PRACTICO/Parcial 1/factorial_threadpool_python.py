# Importa el módulo concurrent.futures para trabajar con hilos (threads)
import concurrent.futures
# Importa el módulo math para usar la función factorial
import math
# Importa el módulo time para medir el tiempo de ejecución
import time

# --- Perfilado (@profile) ---
# Opción A (CPU, línea por línea): ejecutar con kernprof
#   py -m kernprof -l -v .\factorial_threadpool_python.py
#
# Opción B (memoria): DESCOMENTAR la siguiente línea
from memory_profiler import profile
#
# Si no hay ni kernprof ni memory_profiler, @profile queda como no-op.
try:
    profile  # si kernprof/memory_profiler ya lo definieron, lo usamos
except NameError:
    def profile(func):  # no-op
        return func

# Función que calcula el factorial de un número n
def factorial(n):
    return math.factorial(n)

# Punto de entrada principal del script
if __name__ == "__main__":
    # Crea una lista de números del 1 al 100
    numbers = list(range(1, 101))
    # Guarda el tiempo de inicio
    start = time.time()

    @profile
    def _thread_pool():
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(factorial, numbers))
        return results

    results = _thread_pool()

    # Guarda el tiempo de finalización
    end = time.time()
    # Imprime los resultados de los factoriales
    for n, f in zip(numbers, results):
        print(f"{n}! = {f}")
    # Imprime el tiempo total de ejecución
    print(f"Tiempo total usando ThreadPoolExecutor: {end - start:.4f} segundos")
