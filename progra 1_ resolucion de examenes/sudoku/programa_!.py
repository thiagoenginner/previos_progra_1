import random
def generar_matriz(n, desde=100, hasta=999):
    matriz = [[random.randint(desde, hasta) for _ in range(n)] for _ in range(n)]
    
    return matriz

def buscar_menor_valor(matriz):
    menor = 999
    for fila in matriz:
        menor = min(menor, min(fila))
        
    return menor

def crear_lista(matriz):
    lista = []
    for i, fila in enumerate(matriz):
        lista += fila[i:]
    
    return lista

def imprimir_matriz(matriz):
    for fila in matriz:
        print(*fila)
        
#pp
n_input=int(input("tamaño: "))
if 0 < n_input < 20:
    matriz = generar_matriz(n_input)
    imprimir_matriz(matriz)

    print(buscar_menor_valor(matriz))
    print(crear_lista(matriz))

