lista = []
while True:
    n = lista.append(int(input("Digite um valor : ")))
    a = str(input("Quer continuar ? [S/N] : ")).strip().upper()
    if a in 'N':
        break
print(f'você digito {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')

