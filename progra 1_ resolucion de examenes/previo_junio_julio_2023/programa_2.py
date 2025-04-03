es_oblongo = lambda n: sum(x * (x + 1) == n for x in range(int(n ** 0.5) + 1)) > 0

#programa principal
numero = int(input("Ingrese un número entero (-1 para salir): "))
while numero != -1:
    if es_oblongo(numero):
        print(f"{numero} es oblongo.")
    else:
        print(f"{numero} no es oblongo.")
    
    numero = int(input("Ingrese un número entero (-1 para salir): "))