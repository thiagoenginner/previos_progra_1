def sumar_numeros(numeros): #Funcion recursiva.
    if not numeros:
        return 0
    if len(numeros) == 1: #caso base: situacion que termina con el bucle.
        return numeros[0]
    else: #caso recursivo: situacion que achica el problema.
        return numeros[0] + sumar_numeros(numeros[1:])
    
#programa principal

numeros = []

while True:
    numero = int(input("Ingrese un numero impar o -1 para terminar: "))
    if numero == -1:
        break
    else:
        numeros.append(numero)
    
    
suma= sumar_numeros(numeros)
print(f"Suma: {suma}")