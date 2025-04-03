'''
articulos
    clave : codigo del articulo
    valor : diccionario
        clave : descripcion
        valor : descripcion
        clave : meses
        valor : diccionario
            clave : mes
            valor : cantidad solicitida
        
'''

def procesar_archivo(nombre):
    try:
        archivo = open(nombre, "r", encoding="UTF-8")
        articulos = {}
        
        for registro in archivo:
            codigo_articulo, descripcion, fecha, cantidad = registro.strip().split(";")
            mes = fecha.split("/")[1]
            cantidad = int(cantidad)
            if codigo_articulo not in articulos:
                articulos[codigo_articulo] = {"descripcion": descripcion, "meses": {mes: cantidad}}
            elif mes not in articulos[codigo_articulo]["meses"]:
                articulos[codigo_articulo]["meses"][mes] = cantidad
            else:
                articulos[codigo_articulo]["meses"][mes] += cantidad
                
        return articulos
        
    except FileNotFoundError:
        print("Error al intentar abrir el archivo. Es probable que no exista.")
    except IndexError:
        print("Error al intentar procesar un registro del archivo. Es probable que no tenga el formato necesario.")
    except OSError:
        print("Error al intentar abrir el archivo. Es probable que no tenga los permisos necesarios o hayan recursos no disponibles.")
    
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    finally:
        try:
            archivo.close()
        except NameError:
            pass
    
def mostrar_listado(articulos):
    for key, value in articulos:
        meses_ordenados = sorted(value["meses"].items(), key = lambda x: x[1], reverse = True )
        print(f"{value['descripcion']}: {meses_ordenados[0][0]}")
    
#pp

nombre_archivo = "pedidos_(3).txt"
articulos = procesar_archivo(nombre_archivo)
articulos_ordenados = sorted(articulos.items(), key= lambda x: x[1]["descripcion"])

mostrar_listado(articulos_ordenados)