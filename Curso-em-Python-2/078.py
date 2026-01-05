mai = 0
men = 0
lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c]>mai:
            mai = lista[c]
        if lista[c]< men:
            men = lista[c]
print('=-'*35)
print(f'Você digitou os valores : {lista}')
print(f'o maior foi :{mai} \ne o menor foi :{men}')
for i, v in enumerate(lista):
    if v == mai:
        print(f'O maior valor foi digitado na posição: {i}', )
for i, v in enumerate(lista):
    if v == men:
        print(f'O menor valor foi digitado na posição: {i}', end='')