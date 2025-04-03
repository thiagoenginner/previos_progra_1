import random
def generar_lista_por_comprension(cant):
    lista = [random.randint(1,9) for _ in range(cant)]
    return lista

def obtener_triangulo(lista):
    if not lista:
        return lista
    elif len(lista) == 1:
        return [lista]
    else:
        lista_arriba = [lista[i] + lista[i+1] for i in range(len(lista)-1)]
        return [lista] + obtener_triangulo(lista_arriba)
#pp
lista_base = generar_lista_por_comprension(5)
lista_triangulo = obtener_triangulo(lista_base)
lista_triangulo_invertida = lista_triangulo[::-1]

for lista in lista_triangulo_invertida:
    print(lista)