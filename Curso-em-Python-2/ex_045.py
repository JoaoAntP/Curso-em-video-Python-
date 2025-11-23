from random import randint
itens = ('Pedra','Papel','Tesoura')
print('''Sua Jogada
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jog = int(input("Qual e sua jogada :"))
computador = randint(0,2)

print('''

JO
KEN
PO !!!
''')
print('-='*10)

print("O Computador jogo {} e voce jogo {}".format(itens[computador],itens[jog]))

print('-='*10)
if computador ==0: #COMPUTADOR JOGOU PEDRA
    if jog==0:
        print("Empate")
    elif jog==1:
        print("Jogador Ganhou")
    elif jog==2:
        print("Computador Ganhou")
    else:
        print("Jogada Invalida")

elif computador ==1: #COMPUTADOR JOGOU PAPEL
    if jog == 0:
        print("Computador Ganha")
    elif jog == 1:
        print("Empate")
    elif jog == 2:
        print("Voce ganhou Ganhou")
    else:
        print("Jogada Invalida")

elif computador ==2: #COMPUTADOR JOGOU TESOURA
    if jog == 0:
        print("Jogador Ganha")
    elif jog == 1:
        print("Computador Ganhou")
    elif jog == 2:
        print("Empate")
    else:
        print("Jogada Invalida")