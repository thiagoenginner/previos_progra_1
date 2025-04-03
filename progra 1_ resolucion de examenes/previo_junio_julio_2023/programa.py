'''
1) diccionario
        numero de cuenta
        diccionario
            nombre_apellido
            saldo_final
'''

def imprimir_listado(cuentas):
    for numero_cuenta, nombre_apellido, saldo_final in sorted(cuentas, key= lambda x: x[2]):
        print(f"{numero_cuenta};{nombre_apellido};{saldo_final}")
def procesar_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "r", encoding="utf-8")
        archivo_nuevo = open("archivo_generado.csv", "w", encoding="utf-8")
        cuentas_saldos_negativos = []
        for registro in archivo:
            datos = registro.strip().split(";")
            
            numero_cuenta = datos[0]
            nombre_apellido = datos[1]
            movimientos = datos[2:]
            movimientos_flotantes = list(map(float, movimientos))
            saldo_final = sum(movimientos_flotantes)
            
            if saldo_final < 0:
                cuentas_saldos_negativos.append((numero_cuenta, nombre_apellido, saldo_final))
            
            archivo_nuevo.write(f"{numero_cuenta};{nombre_apellido};{saldo_final}\n")
        
        imprimir_listado(cuentas_saldos_negativos)
    except Exception as e:
        print(f"{e}")
    finally:
        try:
            archivo.close()
            archivo_nuevo.close()
        
        except NameError:
            pass
            
#programa principal
nombre_archivo = "movimientos.txt"

procesar_archivo(nombre_archivo)