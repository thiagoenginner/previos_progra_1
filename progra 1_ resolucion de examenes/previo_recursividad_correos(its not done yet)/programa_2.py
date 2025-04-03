
'''
oxv7dw¬3q@gmail.com

'''
try:
    archivo = open("correos.txt", "r", encoding="utf-8")
    cantidad_mails_no_validos = 0
    cantidad_mails_por_pais = {}
    for mail in archivo:
        mail = mail.strip()
        
        if mail.count("@") != 1:
            cantidad_mails_no_validos += 1
            continue
        
        usuario, dominio_completo = mail.split("@")
        
        if not usuario.isalnum():
            cantidad_mails_no_validos +=1
            continue
        
        if not dominio_completo or dominio_completo.count(".") == 0 or dominio_completo[0] == "." or dominio_completo[-1] == ".":
            cantidad_mails_no_validos += 1
            continue
        
        partes = dominio_completo.split(".")
        pais = "us"
        if len(partes) == 3 and len(partes[2]) == 2:
            pais = partes[2]
        
        cantidad_mails_por_pais[pais] = cantidad_mails_por_pais.get(pais, 0) + 1
    print("Correos no válidos:", cantidad_mails_no_validos)
    print("Correos por país:", cantidad_mails_por_pais)
except Exception as e:
    print(e)
    
finally:
    try:
        archivo.close()
    except NameError:
        pass