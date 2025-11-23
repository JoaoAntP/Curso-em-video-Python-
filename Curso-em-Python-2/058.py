from random import randint
computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10 ser que você consegue adivinhar")
acertou = False
tentativa = 0
while not acertou:
    n_jogador = int(input("Qual sera seu palpite ?"))
    if n_jogador == computador:
        print("Acertou")
        tentativa =+1
    else:
        if n_jogador > computador:
            print("Mais.. Tente de novo")
            tentativa = +1
        elif n_jogador < computador:
            print("Menos... Tente denovo")
            tentativa = +1
        else:
            print("Erro")
            print("Você acertou com {} tentativas".format(tentativa))
