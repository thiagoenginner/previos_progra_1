def registrar_alquiler(DNI, numero_bicicleta, numero_casco):
    try:
        archivo_historico = open("archivo_historico_alquileres.csv", "a", encoding="utf-8")
        archivo_historico.write(";".join((DNI, numero_bicicleta, numero_casco)) + "\n")
    except FileNotFoundError:
        print("No se pudo abrir el archivo.")
    except Exception as e:
        print("Ocurrio un error inesperado a la hora de registrar el alquiler.")
    finally:
        try:
            archivo_historico.close()
        except NameError:
            pass
        
def alquilar(alquileres):
    try:
        numero_bicicleta = input("Numero de la bicicleta: ").strip()
        numero_casco = input("Numero del casco: ").strip()
        
        if alquileres["bicicletas"][numero_bicicleta]["disponibilidad"] and alquileres["cascos"][numero_casco]["disponibilidad"]:
            print("Combinacion disponible.")
            
            DNI = input("DNI: ").strip()
            
            alquileres["bicicletas"][numero_bicicleta]["disponibilidad"] = False
            alquileres["bicicletas"][numero_bicicleta]["DNI"] = DNI
            alquileres["bicicletas"][numero_bicicleta]["cantidad de alquileres"] += 1
                
            
            alquileres["cascos"][numero_casco]["disponibilidad"] = False
            alquileres["cascos"][numero_casco]["DNI"] = DNI
            alquileres["cascos"][numero_casco]["cantidad de alquileres"] += 1
            
            registrar_alquiler(DNI, numero_bicicleta, numero_casco)
            
            print("Combinacion alquilada con exito.")
   
        else:
            print("Combinacion no disponible.")
        
        return alquileres
    
    except KeyError:
        print("Bicicleta y/o casco inexistente/s.")
    except Exception as e:
        print(f"Ocurrio un error inesperado al intentar alquilar los articulos: {e}")
    return alquileres

def devolver(alquileres):
    try:
        numero_bicicleta = input("Numero de la bicicleta: ").strip()
        numero_casco = input("Numero del casco: ").strip()
    
        if not alquileres["bicicletas"][numero_bicicleta]["disponibilidad"] and not alquileres["cascos"][numero_casco]["disponibilidad"]:
            alquileres["bicicletas"][numero_bicicleta]["disponibilidad"] = True
            alquileres["bicicletas"][numero_bicicleta]["DNI"] = ""            
            
            alquileres["cascos"][numero_casco]["disponibilidad"] = True
            alquileres["cascos"][numero_casco]["DNI"] = ""
        
            print("Devolucion exitosa.")
    
        else:
            print("Hay un articulo que no ha sido alquilado.")
    
    except KeyError:
        print("Bicicleta y/o casco inexistente/s.")
    except Exception as e:
        print(f"Ocurrio un error inesperado al intentar devolver los articulos: {e}")
        
    return alquileres

def cierre_del_dia(alquileres):
    articulos = list(alquileres["bicicletas"].items()) + list(alquileres["cascos"].items())
    print("Elementos con mayor cantidad de alquileres:")
    for elemento, datos in sorted(articulos, key= lambda x: x[1]["cantidad de alquileres"], reverse = True):
        print(f"{elemento}: {datos['cantidad de alquileres']}")
        
    print("Clientes que aun no devolvieron su articulo alquilado:")
    for articulo in articulos:
        if not articulo[1]["disponibilidad"]:
            print(f"El articulo {articulo[0]} aun no fue devuelto. Sigue en el poder de {articulo[1]['DNI']}")
#programa principal

print("1. Alquilar")
print("2. Devolver")
print("3. Cierre del dia")
alquileres = {"bicicletas": {
    "778": {
        "disponibilidad": True,
        "DNI": "",
        "cantidad de alquileres": 0
          },
    "799": {
        "disponibilidad": True,
        "DNI": "",
        "cantidad de alquileres": 0
          },
    "734": {
        "disponibilidad": True,
        "DNI": "",
        "cantidad de alquileres": 0
          },
    "713": {
        "disponibilidad": True,
        "DNI": "",
        "cantidad de alquileres": 0
          }
    },
              "cascos": {
    "905": {
        "disponibilidad": True,
        "DNI": "",
        "cantidad de alquileres": 0
        },
    "941": {
        "disponibilidad": True,
        "DNI": "",
        "cantidad de alquileres": 0
          },
    "920": {
        "disponibilidad": True,
        "DNI": "",
        "cantidad de alquileres": 0
          },
    "999": {
        "disponibilidad": True,
        "DNI": "",
        "cantidad de alquileres": 0
          }
              }
                         
                  }
while True:
    opcion_seleccionada = input("Seleccione una opcion ingresando el numero correspondiente: ")
    if opcion_seleccionada == "1":
        alquileres = alquilar(alquileres)
        
    elif opcion_seleccionada == "2":
        alquileres = devolver(alquileres)
    
    elif opcion_seleccionada == "3":
        cierre_del_dia(alquileres)
        break
    else:
        print("Input invalido.")
        
    
    

