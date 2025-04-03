def crear_matriz(filas, columnas):
    matriz = []
    
    for i in range(filas):
        fila = []
        impar = i * 2 + 1  # Primer número impar de la fila
        par = i * 2 + 2        # Primer número par de la fila
        
        for j in range(columnas):
            if j % 2 == 0:  # Posiciones pares → número impar
                fila.append(impar)
                impar += 8
            else:           # Posiciones impares → número par
                fila.append(par)
                par += 8
                
        matriz.append(fila)
    
    return matriz


def aplanar_matriz(matriz):
    if len(matriz) == 1:
        return matriz[0]
    else:
        return matriz[0] + aplanar_matriz(matriz[1:])
    
#programa principal

tamaño = input("tamaño: ")

if not tamaño:
    matriz = crear_matriz(3, 3)
else:
    matriz = crear_matriz(int(tamaño), int(tamaño))

for fila in matriz:
        print(fila)

lista_comprension = [sum(fila) for fila in matriz]
print(lista_comprension)

matriz_aplanada = aplanar_matriz(matriz)
print(matriz_aplanada)
    