import random

print('=-'*10)
print("Vamos jogar par ou ímpar")
print('=-'*10)
while True:
    rad = random.randint(1,11)
    jog = int(input("Digite um valor : "))
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Par ou Impar ? [P/I]: ")).upper()
    media1 = jog + rad
    if tipo == 'P':
        if media1 % 2 == 0:
            print(f'Você jogou {jog} e o computador {rad} a soma total foi {media1}, Deu PAR você ganhou!!')
        else:
            print(f'Você jogou {jog} e o computador {rad} a soma foi {media1}, você errou!')
    elif tipo == 'I':
        if media1 % 2 == 1:
            print(f'Você jogou {jog} e o computador {rad} a soma total foi {media1}, Deu ÍMPAR você ganhou!!')
        else:
            print(f'Você jogou {jog} e o computador {rad} a soma foi {media1}, você errou!')

