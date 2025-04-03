'''
1) convertir la linea en una lista de palabras
2) iterar sobre la lista de palabras, llamar a una funcion que se encargue de limpiar cada palabra, y, si
tiene mas de tres letras, guardarla en un subdiccionario determinado junto a la cantidad
correspondiente de repeticiones.
3) ordenar el diccionario con una tupla de criterios.
4) recorrer la secuencia de tuplas con un bucle e imprimir cada nombre seguido de su numero de repeticiones.

'''
    
#programa principal
try:
    archivo = open(r"C:\Users\betoa\OneDrive\Desktop\progra 1_ resolucion de examenes\previo_abril_mayo_2023\texto.txt", "r", encoding="UTF-8")
    contador_palabras = {}
    
    for linea in archivo:
        for palabra in linea.strip().split():
            palabra_limpia = "".join(letra for letra in palabra if letra.isalpha()).lower()
            
            if len(palabra_limpia) > 3:
                if palabra_limpia in contador_palabras:
                    contador_palabras[palabra_limpia] += 1
                else:
                    contador_palabras[palabra_limpia] = 1
    for palabra, repeticiones in sorted(contador_palabras.items(), key= lambda x: (len(x[0]), x[0])):
        print(f"{palabra} --> {repeticiones}")

except Exception as e:
    print(e)

finally:
    try:
        archivo.close()
    except NameError:
        pass
            