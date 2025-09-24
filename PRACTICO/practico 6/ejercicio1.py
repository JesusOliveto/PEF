import cProfile

def suma_numeros_naturales(n):
    """Calcula la suma de los primeros n números naturales usando un bucle."""
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# Profiling
if __name__ == "__main__":
    cProfile.run('suma_numeros_naturales(1_000_000)')