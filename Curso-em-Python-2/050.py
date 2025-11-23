cont = 0
soma = 0
for c in range(0,2):
    n=int(input("Digite um numero"))
    if n%2 == 0:
        soma = soma + n
        cont = cont + 1
print("voce informou  {} numero e a soma dos valores foi {}".format(cont, soma))