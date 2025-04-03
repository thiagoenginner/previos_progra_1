# Main program (a function is not necessary since this runs only once)

def quicksort(lista): #  este algoritmo recursivo de ordenamiento es optimo cuando no tenes tanta data y queres algo rapido. no utilizar con listas ordenadas!
    if len(lista) <=1:
        return lista
    
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[1]["total_votos"] >= pivote[1]["total_votos"]]
        mayores = [x for x in lista[1:] if x[1]["total_votos"] < pivote[1]["total_votos"]]
        
        return quicksort(menores) + [pivote] + quicksort(mayores)

archivo = open(r"C:\Users\betoa\Downloads\partidos_politicos_desordenado.csv", "r", encoding = "UTF-8")
votos_partidos_por_alianza = {}
total_votos_general = 0
for registro in archivo:
    registro = registro.strip().split(";") #dividir el registro una sola vez y limpiar al inicio y al final.
    partido_politico, alianza = registro[0], registro[1] 
    if partido_politico not in votos_partidos_por_alianza:
        votos_partidos_por_alianza[partido_politico] = {"alianzas": {alianza: 1}, "total_votos": 1}
    elif alianza in votos_partidos_por_alianza[partido_politico]["alianzas"]:
        votos_partidos_por_alianza[partido_politico]["alianzas"][alianza] +=1
        votos_partidos_por_alianza[partido_politico]["total_votos"] += 1
    else:
        votos_partidos_por_alianza[partido_politico]["alianzas"][alianza] = 1
        votos_partidos_por_alianza[partido_politico]["total_votos"] += 1
    
    total_votos_general += 1
    
partidos_en_orden = quicksort(list(votos_partidos_por_alianza.items()))

for partido in partidos_en_orden:
    porcentaje = partido[1]["total_votos"] * 100 / total_votos_general
    numero_de_asteriscos = porcentaje // 5
    grafico_de_barra = '*' * int(numero_de_asteriscos)
    print(f"{partido[0].ljust(20)} {grafico_de_barra} {porcentaje: .2f}%")

alianzas_ordenadas_partido_ganador = sorted(partidos_en_orden[0][1]["alianzas"].items(), key = lambda item: item[1], reverse = True)
print(f"\nPartido ganador: {partidos_en_orden[0][0]}")

for alianza in alianzas_ordenadas_partido_ganador:
    print(partidos_en_orden[0][1].get("total_votos"))
    porcentaje = alianza[1] * 100 / partidos_en_orden[0][1].get("total_votos")
    numero_de_asteriscos = porcentaje // 5
    grafico_de_barra = '*' * int(numero_de_asteriscos)
    print(f"{alianza[0].ljust(20)} {grafico_de_barra} {porcentaje: .2f}%")

    