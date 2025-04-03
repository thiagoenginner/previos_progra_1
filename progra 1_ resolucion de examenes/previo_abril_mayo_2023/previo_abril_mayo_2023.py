#copiar las lineas originales en una lista.
"""mandar la linea a una funcion que la convierta en un conjunto de palabras  e iterar sobre esta para guardar las palabras
a encerrar en una lista
paso 3: mandar la linea y la tupla a una funcion que encierre en la linea original las palabras en la tupla.
paso 4: escribir la linea en un archivo nuevo."""

def limpiar_palabras(linea):
    lista_palabras = linea.strip().split() # lista con palabras.
    conjunto_palabras_limpias = set() # conjunto vacio, ya que no queremos encerrar mas de una vez las palabras correspondientes.
    
    for palabra in lista_palabras: 
        palabra_limpia = "".join([letra for letra in palabra if letra.isalpha()]) # limpia la palabra: agrega un carcater si es un numero o una letra.
        conjunto_palabras_limpias.add(palabra_limpia) # agrega la palabra limpia al conjunto.
    
    return conjunto_palabras_limpias

def determinar_palabras_a_encerrar(conjunto_palabras_limpias): 
    lista_palabras_a_encerrar = [] #lista vacia.
    for palabra in conjunto_palabras_limpias:
        contador_vocales = sum(1 for letra in palabra if letra.lower() in "aeiouáéíóú") #cuenta la cantidad de vocales incluidas en la palabra.
        
        if contador_vocales > len(palabra)/2:
            lista_palabras_a_encerrar.append(palabra) #agrega la palabra a la lista.
            
    return lista_palabras_a_encerrar
            

def encerrar_palabras(lista_palabras_a_encerrar, linea):
    lista_palabras_linea = linea.strip().split() # lista con las palabras de la linea.
    cadenas_a_copiar = [] #lista que contendra las cadenas a copiar para la linea.
    
    for palabra in lista_palabras_linea:
        palabra_limpia = "".join([letra for letra in palabra if letra.isalnum()]) #limpia una palabra de la linea.
        if palabra_limpia in lista_palabras_a_encerrar:
            palabra = palabra.replace(palabra_limpia, f"({palabra_limpia})") #encierra la palabra
        cadenas_a_copiar.append(palabra) #agrega la palabra encerrada o no a la lista de cadenas a copiar.
    
    return " ".join(cadenas_a_copiar) #une las cadenas en una sola.

#mp

nombre_archivo = "texto.txt"
try:
    archivo = open(nombre_archivo, "r", encoding="UTF-8") #el archivo contiene acentos... xd
    archivo_nuevo = open("ArchivoPalabrasEncerradas.txt", "w", encoding = "UTF-8") #el archivo contiene acentos...
    
    ''' UTF 8 ES UN SISTEMA DE CODIFICACION DE CARACTERES QUE PERMITE REPRESENTAR CASI CUALQUIER CARACTER DE CUALQUIER IDIOMA DEL MUNDO.
     TODOS LOS SISTEMAS OPERATIVOS TIENEN UNO PREDETERMINADO. SI QUERES LEER O ESCRIBIR CARACTERES CON ACENTOS, LA LETRA Ñ Y/O CARACTERES DE OTRO IDIOMA, LO NECESARIO ES
     DECIRLE A TU SISTEMA QUE UTILICE EL SISTEMA DE CODIFICACION UTF-8. ADEMAS, SI ESTAS TRABAJANDO CON UN ARCHIVO QUE CONTIENE UNO DE ESTOS CARACTERES, TAMBIEN
     SERA NECESARIO ESPECIFICAR LA CODIFICACION Y DECODIFICACION CON UTF8.
    '''
    
    for linea_global in archivo:
            
        conjunto_palabras_limpias_global = limpiar_palabras(linea_global) # LIMPIA LA PALABRAS ej: auto, --> auto; "harry --> harry
            #DEVUELVE UN CONJUNTO PARA NO REPETIR DATOS.
            
        lista_palabras_a_encerrar_global = determinar_palabras_a_encerrar(conjunto_palabras_limpias_global) #DETERMINA QUE PALABRAS ENCERRAR ej: auto
            #DEVUELVE UNA LISTA.
            
        linea_con_palabras_encerradas = encerrar_palabras(lista_palabras_a_encerrar_global, linea_global) #ENCIERRA LAS PALABRAS EN LA LINEA ORIGINA ej: auto, --> (auto),
            #DEVUELVE UN STRING.
            
        archivo_nuevo.write(linea_con_palabras_encerradas + "\n") #AGREGA UN SALTO DE LINEA AL STRING Y LO GUARDA EN LA LISTA FINAL.

except FileNotFoundError:
    print(f"El archivo {nombre_archivo} no se encontro.") #el archivo no exite.

except OSError as m:
    print(f"Error en el sistema: {m}") #falta de espcio en la memoria 
    
except Exception as e:
    print(f"Ocurrio un error inesperado: {e}") #falta de permisos para crear o leer, espacio insuficiente

else:
    print("El archivo nuevo fue creado con exito.")
    
finally:
    try:
        archivo.close()
        archivo_nuevo.close()
    except NameError: 
        pass
            