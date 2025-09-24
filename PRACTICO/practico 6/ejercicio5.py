import unittest

def es_primo(n):
    """
    Determina si un número es primo.
    
    Args:
        n (int): Número a evaluar
        
    Returns:
        bool: True si es primo, False en caso contrario
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

class TestEsPrimo(unittest.TestCase):
    """Test cases para la función es_primo"""
    
    def test_numeros_primos(self):
        """Test para números primos conocidos"""
        primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for primo in primos:
            with self.subTest(primo=primo):
                self.assertTrue(es_primo(primo))
    
    def test_numeros_no_primos(self):
        """Test para números no primos"""
        no_primos = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for no_primo in no_primos:
            with self.subTest(no_primo=no_primo):
                self.assertFalse(es_primo(no_primo))
    
    def test_numeros_negativos(self):
        """Test para números negativos"""
        self.assertFalse(es_primo(-1))
        self.assertFalse(es_primo(-7))
    
    def test_cero(self):
        """Test para el número 0"""
        self.assertFalse(es_primo(0))

if __name__ == "__main__":
    unittest.main(verbosity=2)