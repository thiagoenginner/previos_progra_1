import random
def generar_sudoku():
    matriz = [[0 for _ in range (9)] for _ in range(9)]
    numeros = [1,2,3,4,5,6,7,8,9]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = random.choice(numeros)
    return matriz

def imprimir_lista(matriz):
    for fila in matriz:
        print(*fila)

def validar_sudoku(sudoku):
    for i in range(len(sudoku)):
        fila = set()
        columna = set()
        for j in range(len(sudoku[0])):
            fila.add(sudoku[i][j])
            columna.add(sudoku[j][i])
            
        if len(fila) != 9 or len(columna) != 9:
            return False
    return True
#pp

sudoku = generar_sudoku()
imprimir_lista(sudoku)
if validar_sudoku(sudoku):
    print("Sudoku valido.")
else:
    print("Sudoku invalido.")


    
