import random
def procesarLinea(line,dicc,combis):
    if len(line) > 1:
        nombre = line[0]
        fila = int(line[-2])
        asiento = line[-1]
        combi = (fila,asiento)
    else:
        randomcombin = random.choice(combis)
        nombre = line[0]
        asiento = randomcombin[1]
        fila = int(randomcombin[0])
        combi = (fila,asiento)
    dicc[nombre] = combi



def determinarModeloAvion():
    try:
        arch=open(r"C:\Users\lucca\OneDrive\Desktop\previo progra 1\Finales v2.0\Vuelos447.txt",'rt',encoding='utf-8')
        filas = set()
        for line in arch:
            line = line.strip().split(';')
            if len(line) == 3:
                filas.add(int(line[-2]))
        return max(filas)
    except FileNotFoundError:
        print('El archivo no se ha encontrado')


def combinacionesAsientos(modelo):
    if modelo > 30:
        lista = ['A','B','C','D','E','F','G','H','I','J']
    else:
        lista = ['A','B','C','D','E','F']
    combinaciones = [(i,x) for x in lista for i in range(1,modelo)]
    return combinaciones

def asientosLibres(combinaciones,sort):
    for i in combinaciones:
        if i not in list(sort.values()):
            print(f'Han quedado libres los siguientes asientos {i}')


def colisiones(combinaciones,sort):
    lista = []
    for i in combinaciones:
        if list(sort.values()).count(i) > 1:
            lista.append(i)
    print(f'Los asientos con colisiones son {lista}')
    
    
def main(combinaciones):
    try:
        arch=open(r"C:\Users\lucca\OneDrive\Desktop\previo progra 1\Finales v2.0\Vuelos447.txt",'rt',encoding='utf-8')
        dicc={}
        combinaciones  = combinaciones
        for line in arch:
            line = line.strip().split(';')
            procesarLinea(line,dicc,combinaciones)
        sort = dict(sorted(dicc.items(),key=lambda x:(x[1][0],x[1][1])))
        for clave,value in sort.items():
            print(f'La persona "{clave}" tiene asignado el asiento {value[1]} en la fila {value[0]}')
            
        asientosLibres(combinaciones,sort)
        colisiones(combinaciones,sort)
    except FileNotFoundError:
        print('El archivo no ha sido encontrado')
    finally:
        try:
            arch.close()
        except NameError:
            pass
main(combinacionesAsientos(determinarModeloAvion()))