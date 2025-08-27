
import random
import array
import sys
import time
import math
from multiprocessing import Pool
import threading
#from memory_profiler import profile


#@profile
def esPrimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros= [11227253509523, 11227253509529, 11227253509531, 11227253509533, 11227253509537, 11227253509539, 11227253509543]
#numeros=[11227253509523]


def main():
    inicio = time.time()
    resultados= list(map(esPrimo, numeros))
    fin = time.time()
    print(f"Tiempo de ejecucion:                    {fin - inicio} segundos")
    print(f"Resultados: {resultados}")

    # inicio, fin = 0, 0
    # inicio= time.time()
    # with Pool() as pool:
    #     resultados= pool.map(esPrimo, numeros)
    # fin = time.time()
    # print(f"Tiempo de ejecucion con multiprocessing:{fin - inicio} segundos")
    # print(f"Resultados: {resultados}")
    
    # #hilos
    # inicio,fin = 0, 0
    # inicio = time.time()
    # hilos= []
    # for i in range(len(numeros)):
    #     hilo= threading.Thread(target=esPrimo, args=(numeros[i],))
    #     hilos.append(hilo)
    #     hilo.start()
    # for hilo in hilos:
    #     hilo.join()
    # fin = time.time()
    # print(f"Tiempo de ejecucion con hilos:        {fin - inicio} segundos")

if __name__ == "__main__":
    main()
    