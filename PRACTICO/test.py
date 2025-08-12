#mide el tiempo de ejecucion de un algoritmo de fibonacci
import random



def measure_time(sort_function, arr):
    import time
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
    n = 37  # Cambiar este valor para probar con diferentes entradas

    print(f"Tiempo de ejecución: {measure_time(fibonacci, n)} segundos")

    print(f"Tiempo de ejecución (memoizado): {measure_time(fibonacci_memoized, n)} segundos")
    
    print(f"Tiempo de ejecución (iterativo): {measure_time(fibonacci_iterative, n)} segundos")



if __name__ == "__main__":
    main()
    