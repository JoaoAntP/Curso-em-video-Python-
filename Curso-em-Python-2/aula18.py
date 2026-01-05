#teste = list()
#teste.append('João')
#teste.append(20)
#print(teste)
#galera = list()
#galera.append(teste[:])
#galera.append(teste)
#teste[0] = 'Maria'
#teste[1] = 22
#print(galera)
#teste.append()
#teste.append()

#galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 25]]
#print(galera[2][0])
#for p in galera:
#    print(f'{p[0]} tem {p[1]} 'anos de idade'')


totalmai = 0
totalmen = 0
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])#copia os dados
    dado.clear()

for p in galera:
    if p[1]>=18:
        print(f'{p[0]} e Maior de idade')
        totalmai += 1
    else:
        print(f'{p[0]} e menor de idade')
        totalmen += 1
print(f'O numero total de maiores foi {totalmai} e o de menores foi {totalmen}')
print(galera)
