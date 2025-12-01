n = 0
resp = 'S'
soma = quant = media = maior_v = menor_v= 0
while resp in 'Ss':
    n = int(input("Digite um valor:"))
    soma += n
    quant += 1
    if quant == 1:
        maior_v = menor_v = n
    else:
        if n>maior_v:
            maior_v = n
        if n < menor_v:
            menor_v = n
    resp = str(input("Quer continuar ? [S/N]")).upper().strip()[0]
media = soma/quant
print("Você digitou {} números e a média foi {} ".format(quant, media))
print("O maior valor foi {} e o menor foi {}".format(maior_v, menor_v))