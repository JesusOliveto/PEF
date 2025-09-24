from dataclasses import dataclass
from collections import deque


# 1 – Enunciado: Se cuenta con una lista de 1 millón de números enteros únicos y se necesita comprobar si un número dado está en la colección miles de veces. Eligir una estructura de datos que minimice el tiempo total de las búsquedas.


def main_ejercicio_1():
    numeros = set() #utilizando set para O(n) al crear, O(1) al buscar
    for i in range(1_000_000):
        numeros.add(i)
    
    print(999_999 in numeros)
    print(1_000_001 in numeros)

# 2 -  Enunciado: Se necesita almacenar datos de 1 millón de usuarios y poder acceder rápidamente al usuario n° 500,000 sin recorrer la colección.

@dataclass(slots=True)  # slots reduce memoria
class Usuario:
    id: int
    nombre: str
    edad: int

def main_ejercicio_2():
    usuarios = [Usuario(i, f"User {i}", 20 + (i % 50)) for i in range(1_000_000)]
    u = usuarios[499_999] #acceso por indice es siempre O(1)
    print(u)


# 3- Enunciado: Se quiere almacenar datos de productos en el orden en el que llegan, pero también poder buscar un producto por su código en O(1).

@dataclass(slots=True)
class Producto:
    codigo: int
    nombre: str
    precio: float

#dict mantiene el orden de llegada
productos: dict[int, Producto] = {} 

#insercion en O(1)
def alta(prod: Producto) -> None:
    productos[prod.codigo] = prod

#busqueda en O(1) promedio
def buscar(codigo: int) -> Producto | None:
    return productos.get(codigo)

def iterar_en_orden_llegada():
    for p in productos.values():
        yield p
        
def main_ejercicio_3():
    for i in range(1, 6):
        alta(Producto(i, f"Producto {i}", i * 10.0))
    
    print(buscar(3))
    print(buscar(10))
    
    print("Productos en orden de llegada:")
    for p in iterar_en_orden_llegada():
        print(p)


# 4- Enunciado: Se necesita procesar solicitudes en el orden en que llegan, quitando siempre la primera en O(1).

cola = deque() #deque permite O(1) en ambos extremos

def ingresar_solicitud(solicitud: str) -> None:
    cola.append(solicitud)
    
def procesar_solicitud() -> str | None:
    if not cola:
        return None
    return cola.popleft()



def main_ejercicio_4():
    ingresar_solicitud("Solicitud 1")
    ingresar_solicitud("Solicitud 2")
    ingresar_solicitud("Solicitud 3")

    print(procesar_solicitud())
    print(procesar_solicitud())
    print(procesar_solicitud())
    print(procesar_solicitud())



# 5- Enunciado: Se tiene una secuencia de eventos y se quiere eliminar duplicados pero manteniendo el orden original.

eventos = []

def agregar_evento(evento: str) -> None:
    eventos.append(evento)

def eliminar_duplicados(lista) -> None:
    vistos = set()
    out = []
    for x in lista:          # O(n)
        if x not in vistos:  # O(1)
            vistos.add(x)
            out.append(x)
    eventos[:] = out

def main_ejercicio_5():
    agregar_evento("Evento 1")
    agregar_evento("Evento 2")
    agregar_evento("Evento 1")
    agregar_evento("Evento 3")
    agregar_evento("Evento 2")

    print("Eventos antes de eliminar duplicados:", eventos)
    eliminar_duplicados(eventos)
    print("Eventos después de eliminar duplicados:", eventos)

if __name__ == "__main__":
    print("Ejercicio 1:")
    main_ejercicio_1()
    print("Ejercicio 2:")
    main_ejercicio_2()
    print("Ejercicio 3:")
    main_ejercicio_3()
    print("Ejercicio 4:")
    main_ejercicio_4()
    print("Ejercicio 5:")
    main_ejercicio_5()