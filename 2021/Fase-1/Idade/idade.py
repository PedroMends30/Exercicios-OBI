idade = [0, 0, 0]

idade[0] = input()
idade[1] = input()
idade[2] = input()

def getMiddleElement(idade):
    idade.sort()
    return idade[1]

print(getMiddleElement(idade))   

    