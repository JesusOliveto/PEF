#EJERCICIOS DE MEMOIZACION

def measure_time(sort_function, arr):
    import time
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time


#EJERCICIO 1: 1 -Dada una cuadrícula de tamaño m x n, escribí una función que devuelva la cantidad de formas de llegar desde la esquina superior izquierda (0,0) a la inferior derecha (m-1,n-1), moviendo solo hacia la derecha o hacia abajo.


def contarCaminosIterativo(m, n):

    matriz = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            matriz[i][j] = matriz[i - 1][j] + matriz[i][j - 1]
            
    return matriz[m - 1][n - 1]

def contarCaminosMemo(m, n, memo={}):
    if m == 1 or n == 1:
        return 1
    
    if (m, n) in memo:
        return memo[(m, n)]
    
    memo[(m, n)] = contarCaminosMemo(m - 1, n, memo) + contarCaminosMemo(m, n - 1, memo)
    return memo[(m, n)]




def main_ejercicio_1():
    m, n = 255, 255
    print("EJERCICIO 1: Cantidad de caminos en una cuadrícula (255x255)")
    print(f"Tiempo de ejecución (memoizado): {measure_time(lambda x: contarCaminosMemo(m, n), None)} segundos")
    print(f"Tiempo de ejecución (iterativo): {measure_time(lambda x: contarCaminosIterativo(m, n), None)} segundos")

    print(f"Cantidad de caminos (memoizado): {contarCaminosMemo(m, n)}")
    print(f"Cantidad de caminos (iterativo): {contarCaminosIterativo(m, n)}")
    

#EJERCICIO 2: 2-Dada una lista de enteros positivos y un número objetivo, escribí una función que determine si existe un subconjunto cuya suma sea exactamente el objetivo.


def existeSubconjuntoIterativo(numeros, objetivo):
    
    matriz = [False] * (objetivo + 1)
    matriz[0] = True

    for num in numeros:
        for i in range(objetivo, num - 1, -1):
            matriz[i] = matriz[i] or matriz[i - num]

    return matriz[objetivo]

def existeSubconjuntoMemo(numeros, objetivo, n=None, memo={}):
    if n is None:
        n = len(numeros)
    
    if objetivo == 0:
        return True
    if n == 0:
        return False
    
    if (n, objetivo) in memo:
        return memo[(n, objetivo)]
    
    if numeros[n - 1] > objetivo:
        memo[(n, objetivo)] = existeSubconjuntoMemo(numeros, objetivo, n - 1, memo)
    else:
        memo[(n, objetivo)] = (existeSubconjuntoMemo(numeros, objetivo - numeros[n - 1], n - 1, memo) or
                              existeSubconjuntoMemo(numeros, objetivo, n - 1, memo))
    
    return memo[(n, objetivo)]

def main_ejercicio_2():
    import random
    numeros = [random.randint(1, 100) for _ in range(100)]
    objetivo = 1000
    print("EJERCICIO 2: Existe subconjunto con suma objetivo")
    print(f"Números: {numeros}")
    print(f"Objetivo: {objetivo}")
    print(f"Tiempo de ejecución (memoizado): {measure_time(lambda x: existeSubconjuntoMemo(numeros, objetivo), None)} segundos")
    print(f"Tiempo de ejecución (iterativo): {measure_time(lambda x: existeSubconjuntoIterativo(numeros, objetivo), None)} segundos")
    print(f"Existe subconjunto (memoizado): {existeSubconjuntoMemo(numeros, objetivo)}")
    print(f"Existe subconjunto (iterativo): {existeSubconjuntoIterativo(numeros, objetivo)}")




#EJERCICIO 3: 3-Dado un string s y una lista de palabras válidas, determiná si s se puede formar usando solo palabras de la lista, reutilizándolas si es necesario.

def puedeFormarPalabraIterativo(s, palabras):
    n = len(s)
    matriz = [False] * (n + 1)
    matriz[0] = True

    for i in range(1, n + 1):
        for palabra in palabras:
            if matriz[i - len(palabra)] and s[i - len(palabra):i] == palabra:
                matriz[i] = True
                break

    return matriz[n]


def puedeFormarPalabraMemo(s, palabras, memo={}):
    if s == "":
        return True
    
    if s in memo:
        return memo[s]
    
    for palabra in palabras:
        if s.startswith(palabra):
            if puedeFormarPalabraMemo(s[len(palabra):], palabras, memo):
                memo[s] = True
                return True
    
    memo[s] = False
    return False

def main_ejercicio_3():
    s = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
    palabras = ["e"] * 1000000 + ["f"]
    print("EJERCICIO 3: Puede formar palabra")
    print(f"String: {s}")
    #print(f"Palabras: {palabras}")
    print(f"Tiempo de ejecución (memoizado): {measure_time(lambda x: puedeFormarPalabraMemo(s, palabras), None)} segundos")
    print(f"Tiempo de ejecución (iterativo): {measure_time(lambda x: puedeFormarPalabraIterativo(s, palabras), None)} segundos")
    print(f"Puede formar palabra (memoizado): {puedeFormarPalabraMemo(s, palabras)}")
    print(f"Puede formar palabra (iterativo): {puedeFormarPalabraIterativo(s, palabras)}")



#EJERCICIO 4: Dado un valor total y una lista de monedas, escribí una función que devuelva cuántas combinaciones distintas de monedas suman ese total.

def contarCombinacionesMonedasIterativo(total, monedas):
    combinaciones = [0] * (total + 1)
    combinaciones[0] = 1

    for moneda in monedas:
        for i in range(moneda, total + 1):
            combinaciones[i] += combinaciones[i - moneda]

    return combinaciones[total]

def contarCombinacionesMonedasMemo(total, monedas, n=None, memo={}):
    if n is None:
        n = len(monedas)
    
    if total == 0:
        return 1
    if total < 0 or n <= 0:
        return 0
    
    if (total, n) in memo:
        return memo[(total, n)]
    
    memo[(total, n)] = contarCombinacionesMonedasMemo(total - monedas[n - 1], monedas, n, memo) + \
                       contarCombinacionesMonedasMemo(total, monedas, n - 1, memo)
    
    return memo[(total, n)]

def main_ejercicio_4():
    total = 90000
    monedas = [1, 5, 10, 25, 50, 100]
    print("EJERCICIO 4: Contar combinaciones de monedas")
    print(f"Total: {total}")
    print(f"Monedas: {monedas}")
    print(f"Tiempo de ejecución (memoizado): {measure_time(lambda x: contarCombinacionesMonedasMemo(total, monedas), None)} segundos")
    print(f"Tiempo de ejecución (iterativo): {measure_time(lambda x: contarCombinacionesMonedasIterativo(total, monedas), None)} segundos")
    print(f"Combinaciones (memoizado): {contarCombinacionesMonedasMemo(total, monedas)}")
    print(f"Combinaciones (iterativo): {contarCombinacionesMonedasIterativo(total, monedas)}")

if __name__ == "__main__":
    main_ejercicio_1()
    main_ejercicio_2()
    main_ejercicio_3()
    main_ejercicio_4()

