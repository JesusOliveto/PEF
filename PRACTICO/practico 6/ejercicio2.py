import cProfile

from ejercicio1 import suma_numeros_naturales

def suma_numeros_naturales_optimizada(n):
    """Calcula la suma usando la fórmula matemática: n*(n+1)/2"""
    return n * (n + 1) // 2

# Comparación con profiling
if __name__ == "__main__":
    print("=== Versión con bucle ===")
    cProfile.run('suma_numeros_naturales(1_000_000)')
    
    print("\n=== Versión optimizada ===")
    cProfile.run('suma_numeros_naturales_optimizada(1_000_000)')
    
    # Verificación de resultados
    resultado1 = suma_numeros_naturales(1000)
    resultado2 = suma_numeros_naturales_optimizada(1000)
    print(f"\nResultado bucle: {resultado1}")
    print(f"Resultado fórmula: {resultado2}")
    print(f"¿Coinciden? {resultado1 == resultado2}")