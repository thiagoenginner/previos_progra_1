#guardar el nombre y la cant. de unidades.
#guardar el stock en en diccionario, modificandolo con la cant. de unidades.
#definir una funcion que imprima el listado (primero ordenar el diccionario)

#2° tarea:
#guardar el precio y la cantidad, si el año es 2009.
#multiplicar ambos valores y acumular el resultado en una variable resultado.
def imprimir_stock_productos(stock_productos):
    stock_productos_ordenado = sorted(stock_productos.items(), key= lambda stock: stock[1], reverse=True)
    for nombre, stock in stock_productos_ordenado:
        print(f"Nombre: {nombre}. Stock: {stock}\n")
        
#programa principal
try:
    archivo = open("mercaderias.txt", "r", encoding="utf-8")
    stock_productos= {}
    resultado = 0
    for registro in archivo:
        registro = registro.strip()
        if registro[11].isalpha(): #1° formato (compra)
            nombre_producto = registro[11:31]
            cantidad_unidades = int(registro[32:35])
        
        else: #2° formato (venta)
            nombre_producto = registro[14:34]
            cantidad_unidades= int(registro[11:14]) * -1
        
        if nombre_producto not in stock_productos:
            stock_productos[nombre_producto] = cantidad_unidades
        else:
            stock_productos[nombre_producto] += cantidad_unidades
        
        if registro[6:10] == "2009":
            precio = float(registro[36:])
            total = precio*cantidad_unidades * -1
            resultado += total
            
        
    imprimir_stock_productos(stock_productos)
    print(f"El reultado del ejercicio en 2009 fue: {resultado}")

except FileNotFoundError:
    print("El archivo no se encontro.")
except ValueError:
    print("El archivo no sigue el formato previsto.")
except Exception as e:
    print(e)
    
finally:
    try:
        archivo.close()
    except NameError:
        pass
            