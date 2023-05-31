try:
    tam_mag = str(input())
    tam_mag = tam_mag.split()
    tam_matriz = int(tam_mag[0])
    magnitude = int(tam_mag[1])
except ValueError as ve:
    print("Erro: {}".format(ve))
    exit(1)

matriz = []

for i in range(tam_matriz):
    linha = str(input())
    matriz.append(list(linha))
    matriz[i] = [int(i) for i in matriz[i]]

def avanco_lava (mag : int, map : list):
    for line in map:
        for element in line:
            if int(element) < mag:
                map[element] = "*" 
    return map

print(avanco_lava(magnitude, matriz))

"""
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
    print("\n")
"""