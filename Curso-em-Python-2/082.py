lista = []
par = []
impar = []
while True:
    n = int(input("Digite um valor : "))
    lista.append(n)
    if n %2 == 0:
      par.append(n)
    else:
        impar.append(n)
    a = str(input("Quer continuar ? [S/N] : ")).strip().upper()
    if a in 'N':
        break
print(f'A lista completa foi {lista}')
print(f'Os pares foram{par}')
print(f'Os ímpares foram{impar}')