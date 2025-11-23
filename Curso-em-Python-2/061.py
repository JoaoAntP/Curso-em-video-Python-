print("Gerador de PA")
print('-=-' * 10)

termo = int(input("Digite o Termo da PA : "))
razao = int(input("Digite a razão da PA : "))
ter = termo
cont = 1
while cont <= 10:
    print('{} ->'.format(ter), end='')
    ter += razao
    cont += 1
print(' FIM')