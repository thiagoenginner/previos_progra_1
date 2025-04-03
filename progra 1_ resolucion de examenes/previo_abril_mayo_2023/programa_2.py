es_primo = lambda n: n > 1 and not (False in [n % i != 0 for i in range(2, int(n**0.5) + 1)])

# Pruebas
numeros = [1, 2, 3, 4, 5, 16, 17, 19, 20, 23]
for num in numeros:
    print(f"{num} -> {es_primo(num)}")
