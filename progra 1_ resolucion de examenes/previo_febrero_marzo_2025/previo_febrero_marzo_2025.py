# Main program (a function is not necessary since this runs only once)

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
    
partidos_en_orden = sorted(votos_partidos_por_alianza.items(), key= lambda datos : datos[1]["total_votos"], reverse= True)

for partido in partidos_en_orden:
    porcentaje = partido[1]["total_votos"] * 100 / total_votos_general
    numero_de_asteriscos = porcentaje // 5
    grafico_de_barra = '*' * int(numero_de_asteriscos)
    print(f"{partido[0].ljust(20)} {grafico_de_barra} {porcentaje}%")

alianzas_ordenadas_partido_ganador = sorted(partidos_en_orden[0][1]["alianzas"].items(), key = lambda item: item[1], reverse = True)
print(alianzas_ordenadas_partido_ganador)
print(f"\nPartido ganador: {partidos_en_orden[0][0]}")

for alianza in alianzas_ordenadas_partido_ganador:
    print(partidos_en_orden[0][1].get("total_votos"))
    porcentaje = alianza[1] * 100 / partidos_en_orden[0][1].get("total_votos")
    numero_de_asteriscos = porcentaje // 5
    grafico_de_barra = '*' * int(numero_de_asteriscos)
    print(f"{alianza[0].ljust(20)} {grafico_de_barra} {porcentaje}%")

    