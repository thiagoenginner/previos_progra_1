n =5
matriz = []

for i in range(n):
    fila = []
    for j in range(n):
        valor = min(i, j, n-1-i, n-1-j) + 1
        fila.append(valor)
    matriz.append(fila)

# Imprimir la matriz con formato adecuado
for fila in matriz:
    print("  ".join(map(str, fila)))


    