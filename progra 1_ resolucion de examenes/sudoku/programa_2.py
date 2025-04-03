
def contar_mayusculas(string):
    if not string:
        return 0
    else:
        if string[0].isupper():
            return 1 + contar_mayusculas(string[1:])
        else:
            return contar_mayusculas(string[1:])
#pp
while True:
    contraseña_input= input("contraseña: ").strip()
    if contraseña_input:
        try:
            mayusculas = contar_mayusculas(contraseña_input)
            if not contraseña_input[0].isalpha():
                raise ValueError("el primer caracter no es alfabetico.")
            if mayusculas < 2:
                raise ValueError("falta de mayusculas.")
            
        except ValueError as e:
            print(e)
        
        else:
            print("contraseña valida!")
    else:
        break