qnt_premiados = int(input())
tamanho_camiseta = input()
tamanhos = tamanho_camiseta.split()
tamanhos = [int(i) for i in tamanhos]
camisa_p = 0
camisa_m = 0
for i in range(qnt_premiados):
    if tamanhos[i] == 1:
        camisa_p += 1
    elif tamanhos[i] == 2:
        camisa_m += 1

prem_c_p = int(input())
prem_c_m = int(input())

if camisa_p >= prem_c_p and camisa_m >= prem_c_m:
    print("S")
else:
    print("N")
