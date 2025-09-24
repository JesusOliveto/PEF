from memory_profiler import profile

@profile
def generar_cuadrados_lista(n):
    """Genera una lista con los cuadrados de los primeros n números."""
    cuadrados = []
    for i in range(n):
        cuadrados.append(i ** 2)
    return cuadrados

@profile
def ejecutar_profiling():
    return generar_cuadrados_lista(100000)

if __name__ == "__main__":
    ejecutar_profiling()