import random

#programa principal
simbolos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','*', '#']
random.shuffle(simbolos)

matriz = []
for i in range(4):
    fila = []
    for j in range(3):
        fila.append(simbolos.pop())
    matriz.append(fila)
    
for fila in matriz:
    print(*fila)
