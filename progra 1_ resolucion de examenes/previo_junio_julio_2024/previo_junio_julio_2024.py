""" 1. leer una linea de cada archivo, entrar en un bucle y escribir la que tenga menor legajo.
 2. Ademas, leer una nueva linea solamente del archivo de donde se leyo aquel menor legajo.
3. si los dos registros existen y ninguno tiene un legajo mayor que el otro, guardar el numero de inconsistencias
en un diccionario."""
def mostrar_inconsistencias(alumnos):
    print("Alumnos con inconsistencias:\n")
    
    for legajo, nombre in alumnos.items():
        print(f"- {nombre}. Legajo: {legajo}")
        
try:
    archivo_1 = open("archivo_1.txt", "r", encoding="utf-8")
    archivo_2 = open("archivo_2.txt", "r", encoding="utf-8")
    archivo_unico = open("archivo_unico.txt", "w", encoding="utf-8")
    
    inconsistencias_alumnos = {}
    registros_grabados = 0
    registro_1 = archivo_1.readline().strip()
    registro_2 = archivo_2.readline().strip()
    
    while registro_1 or registro_2:
        if not registro_2 or (registro_1 and registro_1.split(";")[0] < registro_2.split(";")[0]):
            archivo_unico.write(registro_1 + "\n")
            registros_grabados += 1
            registro_1 = archivo_1.readline().strip()
        
        elif not registro_1 or (registro_2 and registro_2.split(";")[0] < registro_1.split(";")[0]):
            archivo_unico.write(registro_2 + "\n")
            registros_grabados += 1
            registro_2 = archivo_2.readline().strip()
            
        else:
            if registro_1.split(";")[0] not in inconsistencias_alumnos:
                inconsistencias_alumnos[registro_1.split(";")[0]] = registro_1.split(";")[1]
        
            registro_1 = archivo_1.readline().strip()
            
    mostrar_inconsistencias(inconsistencias_alumnos)
    print(f"\nCantidad de registros grabados: {registros_grabados}")
    print(f"Cantidad de inconsistencias: {len(inconsistencias_alumnos)}")
    
except Exception as e:
    print(e)
else:
    print("\nEl archivo unico fue creado con exito :).")

finally:
    try:
        archivo_1.close()
        archivo_2.close()
        archivo_unico.close()
    except NameError:
        pass
            
        
