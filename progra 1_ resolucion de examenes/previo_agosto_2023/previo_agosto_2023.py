#1) crear un diccionario articulos con pares codigo-datos, donde los datos son listas que contienen los datos de cada articulo en especifico en una tupla.
#2) ordenar el diccionario articulos de manera ascendente segun las descripciones.
#3) iterar sobre el diccionario, calcular el maximo, el minimo y el promedio, e imprimir el informe.
import time

# Marcar el inicio del tiempo
start_time = time.time()

def procesar_archivo(archivo_nombre):
    try:
        articulos = {}
        archivo = open(archivo_nombre, "r", encoding="UTF-8") #FileNotFoundError is possible here.
        for linea in archivo:
            lista_datos = linea.strip().split(";")
            codigo = lista_datos[0]
            descripcion = lista_datos[1]
            localidad = lista_datos[2]
            provincia = lista_datos[3]
            precio = float(lista_datos[4])
            
            if codigo not in articulos:
                articulos[codigo] = {"descripcion": descripcion, "tuplas": [(localidad, provincia, precio)] }
            else:
                articulos[codigo]["tuplas"].append((localidad, provincia, precio))
        
        return articulos
    
    except FileNotFoundError:
        print("No se encontro el archivo.")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")
        
    finally:
        archivo.close()

def ordenar_articulos(articulos):
    secuencia_ordenada = sorted(articulos.items(), key = lambda item: item[1]["descripcion"])
    articulos_ordenado = {}
    for codigo, datos in secuencia_ordenada:
        articulos_ordenado[codigo] = datos
    return articulos_ordenado

def calcular_maximo_minimo_promedio(articulos_ordenado):
    maximo = 0
    minimo = float('inf')
    suma = 0
    diccionario = {}
    
    for datos in articulos_ordenado.values():
        maximo = 0
        minimo = float('inf')
        suma = 0
        localidad = ''
        provincia = ''
        
        for tupla in datos["tuplas"]:
            if maximo < tupla[2]:
                maximo = tupla[2]
                maximo_localidad = tupla[0]
                maximo_provincia = tupla[1]
                
            if minimo > tupla[2]:
                minimo = tupla[2]
                minimo_localidad = tupla[0]
                minimo_provincia = tupla[1]
            suma += tupla[2]
        
        promedio = suma / len(datos["tuplas"])
        descripcion = datos["descripcion"]
        diccionario[descripcion] = {"maximo":{}, "minimo": {}}
        diccionario[descripcion]["maximo"]["precio"]= maximo
        diccionario[descripcion]["maximo"]["localidad"] = maximo_localidad
        diccionario[descripcion]["maximo"]["provincia"] = maximo_provincia
        diccionario[descripcion]["minimo"]["precio"]= minimo
        diccionario[descripcion]["minimo"]["localidad"] = minimo_localidad
        diccionario[descripcion]["minimo"]["provincia"] = minimo_provincia
        diccionario[descripcion]["promedio"] = promedio
        
    return diccionario
    
def imprimir_informe(informe):
    for descripcion, datos in informe.items():
        print(descripcion)
        print()
        print(f"Maximo: {datos['maximo']['precio']}, localidad: {datos['maximo']['localidad']}, provincia: {datos['maximo']['provincia']}")
        print(f"Minimo: {datos['minimo']['precio']}, localidad: {datos['minimo']['localidad']}, provincia: {datos['minimo']['provincia']}")
        print(f"Promedio: {datos['promedio']}")
        print()
        print()
        
archivo_nombre = "PreciosRelevados.txt"

articulos = procesar_archivo(archivo_nombre)
articulos_ordenado = ordenar_articulos(articulos)
informe = calcular_maximo_minimo_promedio(articulos_ordenado)
imprimir_informe(informe)
end_time = time.time()
execution_time = end_time - start_time
print(f"El tiempo de ejecución es: {execution_time} segundos")