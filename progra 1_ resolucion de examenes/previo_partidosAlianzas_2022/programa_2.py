años_bisiestos = lambda año_entrada, año_entrada_1: [año for año in range(año_entrada, año_entrada_1 + 1) if año % 4==0 and (año % 100 != 0 or año%400==0) ]
print(años_bisiestos(1900, 1950))

