#diccionario anagramas
    #clave: string letras
    #valor: set palabras

'''1. procesar el archivo: leer el archivo, convertir cada linea en una lista de strings, sacarle las comas, tildes y '''
def procesar_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "r", encoding="UTF-8") #debe funcionar con cualquier archivo de texto!
        anagramas = {}
        for linea in archivo:
            lista_palabras = procesar_linea(linea)
            for palabra in lista_palabras:
                letras = "".join(sorted(palabra))
                if letras not in anagramas:
                    anagramas[letras] = {palabra}
                else:
                    anagramas[letras].add(palabra)
        return anagramas
    except FileNotFoundError:
        print("No se logro encontrar el archivo.")
    except Exception as e:
        print(f"Ocurrio un fallo inesperado: {e}")
    finally:
        try:
            archivo.close()
        except NameError:
            pass
            

def procesar_linea(linea):
    palabras = linea.strip().split()
    letras_palabras = []
    if palabras:
        for palabra in palabras:
            palabra = palabra.lower().strip('"').strip(".").strip(",").strip("¿").strip("?").strip(":")
            lista_letras = list(palabra)
            for indice, letra in enumerate(lista_letras):
                if letra not in "abcdefghijklmnñopqrstuvwxyz":
                    lista_letras[indice] = {"á":"a", "é": "e", "í": "i", "ó": "o", "ú": "u"}.get(letra)
            letras = "".join(lista_letras)
            letras_palabras.append(letras)
    return list(letras_palabras)

def imprimir_anagramas(anagramas):
    anagramas = sorted(anagramas.items(), key = lambda tupla: len(tupla[1]), reverse= True)
    for tupla in anagramas:
        print(f"\u2022 {', '.join(tupla[1])}")
#pp
nombre_archivo = "archivo.txt"
anagramas = procesar_archivo(nombre_archivo)
imprimir_anagramas(anagramas)