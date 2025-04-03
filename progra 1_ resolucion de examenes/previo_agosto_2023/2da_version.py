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
                articulos[codigo] = {
                    "descripcion": descripcion,
                    "maximo": (localidad, provincia, precio),
                    "minimo": (localidad, provincia, precio),
                    "suma": precio,
                    "repeticiones": 1
                }
            else:
                if precio > articulos[codigo]["maximo"][2]:
                    articulos[codigo]["maximo"] = (localidad, provincia, precio)
                    
                if precio < articulos[codigo]["minimo"][2]:
                    articulos[codigo]["minimo"] = (localidad, provincia, precio)
                    
                articulos[codigo]["suma"] += precio
                articulos[codigo]["repeticiones"] += 1
            
        
        return articulos
    
    except FileNotFoundError:
        print("No se encontro el archivo.")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")
        
    finally:
        try:
            archivo.close()
        except NameError:
            pass
        
def imprimir_informe(articulos):
    for codigo, datos in sorted(articulos.items(), key = lambda x: x[1]['descripcion']):
        print(f"{datos['descripcion']}")
        print()
        print(f"Maximo: {datos['maximo'][2]}, localidad: {datos['maximo'][0]}, provincia: {datos['maximo'][1]}")
        print(f"Minimo: {datos['minimo'][2]}, localidad: {datos['minimo'][0]}, provincia: {datos['minimo'][1]}")
        print(f"Promedio: {datos['suma']// datos['repeticiones']}")
        print()
        print()
        
archivo_nombre = "PreciosRelevados.txt"

articulos = procesar_archivo(archivo_nombre)
imprimir_informe(articulos)
end_time = time.time()
execution_time = end_time - start_time
print(f"El tiempo de ejecución es: {execution_time} segundos")
