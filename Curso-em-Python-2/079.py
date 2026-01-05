valor = []
while True:
    n = (int(input("Digite um valor: ")))
    if n not in valor:
     valor.append(n)
    else:
        print("Esse valor ja está na lista")
    cont = str(input("Deseja continuar ? [S/N]")).upper().strip()
    if cont == 'N':
        break
valor.sort()
print(valor)