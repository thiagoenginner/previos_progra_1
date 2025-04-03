def contar_cantidad_elementos(conjunto):
    try:
        conjunto.pop()
        return 1 + contar_cantidad_elementos(conjunto)

    except KeyError:
        return 0

print(contar_cantidad_elementos({1,2,3,4,5,6,7,8}))