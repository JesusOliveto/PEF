from memory_profiler import profile

def generar_cuadrados_generador(n):
    """Generador que produce cuadrados uno a la vez."""
    for i in range(n):
        yield i ** 2

@profile
def usar_generador():
    """Función que usa el generador y muestra el consumo de memoria."""
    gen = generar_cuadrados_generador(100000)
    suma = 0
    for cuadrado in gen:
        suma += cuadrado
    return suma

@profile
def usar_lista():
    """Función que usa lista para comparar."""
    lista = [i ** 2 for i in range(100000)]
    return sum(lista)

if __name__ == "__main__":
    print("=== Con generador ===")
    resultado_gen = usar_generador()
    
    print("\n=== Con lista ===")
    resultado_lista = usar_lista()
    
    print(f"\nResultado generador: {resultado_gen}")
    print(f"Resultado lista: {resultado_lista}")