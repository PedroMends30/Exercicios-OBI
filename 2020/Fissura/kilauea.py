inputString = input()
N = int(inputString.split()[0]) # Tamanho da Matriz Quadrada
F = int(inputString.split()[1]) # Força da Erupção

# Matriz Quadrada
matriz = []
for i in range(N):
    line = input()
    matriz.append(list(line))
    matriz[i] = [int(x) for x in matriz[i]]

pilha = []

for i in range(N):
    for j in range(N):
        if matriz[i][j] == F:
            pilha.append([i,j])

print(matriz)