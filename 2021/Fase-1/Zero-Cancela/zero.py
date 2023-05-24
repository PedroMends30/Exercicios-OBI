qntNum = int(input())
soma = []

def mostraPilha(pilha):
    for i in range(len(pilha)):
        print(pilha[i], end=" ")
    print()

for i in range(qntNum):
    num = int(input())
    if num != 0:
        soma.append(num)
    else:
        soma.pop()

print(sum(soma))