# 🔹 Ejercicio 2: Aplicar PEP 8 y verificar con flake8

# Código inicial (malo):
# def Suma(a,b):return a+b
# print(Suma(3,4))

# 👉 Tarea: Corregir con PEP 8 y usar flake8 para comprobar.

def suma(a, b):
    """
    Suma dos números.

    Args:
        a (int, float): Primer número.
        b (int, float): Segundo número.

    Returns:
        int | float: La suma de a y b.
    """
    return a + b


print(suma(3, 4))
