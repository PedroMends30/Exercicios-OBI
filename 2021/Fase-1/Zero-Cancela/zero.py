qntNum = int(input("Quantos números você quer somar? "))
soma = []

def mostraPilha(pilha):
    for i in range(len(pilha)):
        print(pilha[i], end=" ")
    print()

for i in range(qntNum):
    num = int(input("Digite um número: "))
    if num != 0:
        soma.append(num)
        mostraPilha(soma)
        print(f"Soma Atual: {sum(soma)}\n")
    else:
        soma.pop()
        mostraPilha(soma)
        print(f"Soma Atual: {sum(soma)}\n")

print(f"Soma final: {sum(soma)}")