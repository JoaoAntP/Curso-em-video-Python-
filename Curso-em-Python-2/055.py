maior = 0
menor = 0
for p in range(1, 3):
    peso = float(input("Digite o pesso de cada pessoa".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
           maior = peso
        if peso < menor:
           menor = peso
print("o maior peso {}".format(maior))
print("o menor peso {}".format(menor))