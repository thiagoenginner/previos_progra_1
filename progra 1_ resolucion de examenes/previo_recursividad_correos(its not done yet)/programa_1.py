def filtrar_vocales(palabra):
    if not palabra:
        return []
    
    letra = palabra[0].lower()
    resto = palabra[1:]
    if letra in "aeiouáéíúó" and palabra.lower().count(letra) == 1:
        return [letra] + filtrar_vocales(resto)
    else:
        return filtrar_vocales(resto)
    
while True:
    palabra_input = input("palabra (o -1 para terminar): ")
    
    if palabra_input == "-1":
        print("Saliendo del programa...")
        break
    else:
        print(filtrar_vocales(palabra_input))
