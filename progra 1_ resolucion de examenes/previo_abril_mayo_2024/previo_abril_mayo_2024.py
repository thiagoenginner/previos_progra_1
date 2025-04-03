#1) crear 5 variables: precio_maximo, precio_minimo, cantidad_precios, suma_precios, nombre_articulo. crear un diccionario: articulos_precios_promedio.
#2) leer el archivo e ir actualizando las 5 variables.
#3) guardar el nombre y el precio promedio del articulo en el diccionario una vez terminado de leerlo.
#4) imprimir el nombre, precio maximo, minimo y promedio del articulo.
#5) subir los pares nombre-precio del diccionario a un archivo nuevo de tipo csv.
#6) ordenar el diccionario segun los precios promedio e imprimir los primeros 10 pares.

#Main program

precio_maximo = 0
precio_minimo = float("inf")
cantidad_precios = 0
suma_precios = 0
nombre_articulo = ""
precios_promedio_articulos = {}
hay_datos = False
archivo = open("PreciosCABA.txt", "r", encoding="UTF-8")

for linea in archivo:
    linea = linea.strip() #removes spaces, tabs and newlines from the beginning and the end.
    if not linea.isdigit():
        if hay_datos:
            print(nombre_articulo)
            print(f"Precio maximo: {precio_maximo}")
            print(f"Precio minimo: {precio_minimo}")
            precio_promedio = suma_precios/cantidad_precios
            print(f"Precio promedio: {precio_promedio:.2f}")
            print()
            precios_promedio_articulos[nombre_articulo] = precio_promedio
            precio_maximo = 0
            precio_minimo = float("inf")
            cantidad_precios = 0
            suma_precios = 0
            
        nombre_articulo = linea
        hay_datos = True 
    else:
        precio = int(linea)
        cantidad_precios += 1
        suma_precios += precio
        precio_maximo = max(precio_maximo, precio)
        precio_minimo = min(precio_minimo, precio)

print(nombre_articulo)
print(f"Precio maximo: {precio_maximo}")
print(f"Precio minimo: {precio_minimo}")
print(f"Precio promedio: {suma_precios/cantidad_precios}")
print()
precios_promedio_articulos[nombre_articulo] = suma_precios/cantidad_precios
            
archivo_csv = open("archivo.csv", "w", encoding="UTF-8") #why do we always use UTF-8 and not another one?
for nombre, precio_promedio in precios_promedio_articulos.items():
    archivo_csv.write(f"{nombre};{precio_promedio:.2f}\n")
archivo_csv.close()
precios_promedio_articulos_ordenado = sorted(precios_promedio_articulos.items(), key = lambda item: item[1], reverse = True)
print("Los 10 articulos mas costosos:")
for index, (nombre, precio_promedio) in enumerate(precios_promedio_articulos_ordenado[:10]): #[:10] el diez esta excluido
    print(f"{index+1}. {nombre}, Precio promedio: ${precio_promedio:.2f}\n")

