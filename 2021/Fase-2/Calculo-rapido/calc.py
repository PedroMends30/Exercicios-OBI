def sumOfAlg (number):
    sum = 0
    number = str(number)
    for i in range(len(number)):
        sum += int(number[i])
    return sum

def sumEqualBetween(sum, min, max):
    count = 0
    for i in range(min, max + 1):
        if sumOfAlg(i) == sum:
            count += 1
    return count

soma = int(input("Digite o valor a ser procurado: "))
min = int(input("Digite o inicio do intervalo a ser procurado: "))
max = int(input("Digite o fim do intervalo a ser procurado: "))

print(f"Existe(em) {sumEqualBetween(soma, min, max)} numero(s) entre {min} e {max} cuja soma dos algarismos é {soma}")