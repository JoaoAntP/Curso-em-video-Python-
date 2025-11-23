print("Gerador de PA")
print('-=-' * 10)

termo = int(input("Digite o Termo da PA : "))
razao = int(input("Digite a razão da PA : "))
ter = termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total+mais
    while cont <= total:
        print('{} ->'.format(ter), end='')
        ter += razao
        cont += 1
    print(' PAUSA')
    mais = int(input("Quantos termos você quer mostrar a mais ? : "))
print(' FIM')