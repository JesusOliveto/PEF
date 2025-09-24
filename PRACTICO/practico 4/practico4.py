
import random
import array
import sys
import time
import math
from multiprocessing import Pool
import threading
from concurrent.futures import ThreadPoolExecutor

# Ejercicio 1: Se tiene un archivo de texto con millones de registros (cada línea es un registro). Escribe un programa en Python que lea el archivo de forma eficiente en lotes de 100 líneas y procese cada lote imprimiendo cuántas líneas contiene.

def procesar(batch):
    return len(batch)

def batcher(lista, batch_size):
    for i in range(0, len(lista), batch_size):
        yield lista[i:i + batch_size]

def main_ejercicio_1():
    inicio = time.time()
  
    datos=list(range(1,10100000))

    with ThreadPoolExecutor() as executor:
        resultados = list(executor.map(procesar, batcher(datos, 100)))

    print("Resultados:", resultados)
    print("Total de líneas:", sum(resultados))
    print("Tiempo:", time.time() - inicio)
    
    
# Ejercicio 2: Dada una lista de números del 1 al 50, divídela en lotes de 10 y calcula la suma de cada lote.
# Salida esperada:
# Lote 1: [1,2,...,10] → Suma: 55
# Lote 2: [11,...,20] → Suma: 155
# ...
# Lote 5: [41,...,50] → Suma: 455

def procesar2(lote):
    return sum(lote)

def main_ejercicio_2():
    datos = list(range(1, 51))
    with ThreadPoolExecutor() as executor:
        resultados = list(executor.map(procesar2, batcher(datos, 10)))
    for i, resultado in enumerate(resultados, 1):
        print(f"Lote {i}: {list(batcher(datos, 10))[i-1]} → Suma: {resultado}")
        
# Ejercicio 3: Simula que tienes que insertar 1000 registros en una base de datos. En lugar de insertar de a uno, agrúpalos en lotes de 200. Imprime cada lote cuando se "inserte".

def procesar3(lote):
    print(f"Inserción de lote: {lote}")

def main_ejercicio_3():
    datos = list(range(1, 1001))
    with ThreadPoolExecutor() as executor:
        resultados = list(executor.map(procesar3, batcher(datos, 200)))
        print("Inserción de registros completada.")
        



# Ejercicio 4: Supongamos que tienes una cola de 27 mensajes. Envía los mensajes en lotes de 5 y marca cada lote como "enviado".
# Salida:
# Enviando lote 1: ['msg_1', ..., 'msg_5']
# Enviando lote 2: ['msg_6', ..., 'msg_10']
# ...
# Enviando lote 6: ['msg_26', 'msg_27']

def procesar4(lote):
    print(f"Enviando lote {lote[0]}: {lote[1]}")

def main_ejercicio_4():
    mensajes = [f"msg_{i}" for i in range(1, 28)]
    with ThreadPoolExecutor() as executor:
        resultados = list(executor.map(procesar4, batcher(mensajes, 5)))
        print("Todos los lotes enviados.")


# Ejercicio 5: Dada una lista de 100 números, procesa los datos en lotes de 20 usando paralelismo con concurrent.futures.
# Cada lote debe calcular la suma de sus elementos.

def procesar5(lote):
    return sum(lote)

def main_ejercicio_5():
    datos = list(range(1, 101))
    with ThreadPoolExecutor() as executor:
        resultados = list(executor.map(procesar5, batcher(datos, 20)))
    for i, resultado in enumerate(resultados, 1):
        print(f"Lote {i}: {list(batcher(datos, 20))[i-1]} → Suma: {resultado}")

def main():
    #main_ejercicio_1()
    #main_ejercicio_2()
    #main_ejercicio_3()
    #main_ejercicio_4()
    main_ejercicio_5()



if __name__ == "__main__":
    main()
    