temp = list()
princ = list()
mai = men = 0
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(int(input('Digite seu peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1]>mai:
            mei = temp[1]
        if temp[1]<men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    cont = str(input('Quer continuar? [S/N]')).strip().upper()
    if cont == 'N':
        break

print('=-'*30)
print(f'Os dados foram{princ}')
print(f'Ao todo,você cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi de {mai}Kg')
print(f'O menor peso foi de {men}Kg')