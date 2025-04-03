import random
def generar_conjunto():
    conjunto = set()
    
    while True:
        numero = random.randint(0,1000)
        if numero != 0:
            conjunto.add(numero)
        else:
            break
    
    return conjunto

def vaciar_conjunto_recursivamente(conjunto):
    if not conjunto:
        return 0
    
    else:
        conjunto.pop()
        return 1 + vaciar_conjunto_recursivamente(conjunto)

#programa principal
conj = generar_conjunto()
print(f"El conjunto tenia {vaciar_conjunto_recursivamente(conj)} numeros.")
        
#ACLARACION: QUIZAS EL ENUNCIADO PEDIA CONTAR LOS ELEMENTOS DENTRO DE LA FUNCION RECURSIVA. SI ESE FUE EL CASO, NO DEBI UTILIZAR LEN() Y DEBERIA AJUSTAR EL CODIGO POR ESE LADO.