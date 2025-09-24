import pytest
from ejercicio5 import es_primo  # Importamos la función del ejercicio 5

# Tests usando pytest
def test_numeros_primos():
    """Test para números primos usando pytest"""
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 97]
    for primo in primos:
        assert es_primo(primo) == True

def test_numeros_no_primos():
    """Test para números no primos usando pytest"""
    no_primos = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 100]
    for no_primo in no_primos:
        assert es_primo(no_primo) == False

def test_numeros_especiales():
    """Test para casos especiales"""
    assert es_primo(0) == False
    assert es_primo(1) == False
    assert es_primo(-5) == False

@pytest.mark.parametrize("numero, esperado", [
    (2, True),
    (4, False),
    (17, True),
    (25, False),
    (29, True),
    (1, False),
    (0, False),
])
def test_primos_parametrizados(numero, esperado):
    """Test parametrizado para varios casos"""
    assert es_primo(numero) == esperado