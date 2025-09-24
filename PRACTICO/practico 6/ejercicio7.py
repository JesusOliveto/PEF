def es_primo_doctest(n):
    """
    Determina si un número es primo.
    
    Args:
        n (int): Número a evaluar
        
    Returns:
        bool: True si es primo, False en caso contrario
        
    Examples:
    >>> es_primo_doctest(2)
    True
    
    >>> es_primo_doctest(4)
    False
    
    >>> es_primo_doctest(17)
    True
    
    >>> es_primo_doctest(1)
    False
    
    >>> es_primo_doctest(0)
    False
    
    >>> es_primo_doctest(-5)
    False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def ejecutar_doctest():
    """Ejecuta los doctests incorporados"""
    import doctest
    doctest.testmod(verbose=True)

if __name__ == "__main__":
    ejecutar_doctest()