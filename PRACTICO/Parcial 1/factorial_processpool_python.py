# Importa el módulo concurrent.futures para trabajar con procesos
import concurrent.futures
# Importa el módulo math para usar la función factorial
import math
# Importa el módulo time para medir el tiempo de ejecución
import time

# --- Perfilado flexible (@profile con line_profiler o memory_profiler) ---
# Si ejecutás con:  py -m kernprof -l -v .\factorial_processpool_python.py
#   -> kernprof inyecta builtins.profile y se usa ese decorador.
# Si NO estás con kernprof:
#   -> probamos importar memory_profiler.profile; si no está, usamos un no-op.
try:
    profile  # si existe (inyectado por kernprof), no hacemos nada
except NameError:
    try:
        from memory_profiler import profile as profile  # para perfilar memoria si está disponible
    except Exception:
        def profile(func):  # no-op si no hay ni kernprof ni memory_profiler
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

    # Crea un ProcessPoolExecutor para ejecutar tareas en procesos independientes (paralelismo real)
    @profile
    def _process_pool():
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = list(executor.map(math.factorial, numbers))
        return results

    results = _process_pool()

    # Guarda el tiempo de finalización
    end = time.time()

    # Imprime los resultados de los factoriales
    for n, f in zip(numbers, results):
        print(f"{n}! = {f}")

    # Imprime el tiempo total de ejecución
    print(f"Tiempo total usando ProcessPoolExecutor: {end - start:.4f} segundos")
