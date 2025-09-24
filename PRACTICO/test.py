import doctest


def sumar(a, b):
    """Suma dos números.
    Ejemplo:
    >>> sumar(2, 3)
    5
    >>> sumar(-1, 1)
    0
    >>> sumar(0, 0)
    0
    
    """
    return a + b

def restar(a, b):
    """Resta dos números.
    Ejemplo:
    >>> restar(5, 3)
    2
    >>> restar(0, 0)
    0
    >>> restar(-1, -1)
    0
    """
    return a - b

if __name__ == '__main__':
    doctest.testmod()