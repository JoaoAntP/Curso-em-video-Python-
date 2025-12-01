n_tabuada = 0
while True:
    n_tabuada = int(input("Digite o valor que você deseja ver a tabuada :"))
    if n_tabuada < 0:
        print("Erro")
        break
    for c in range(1, 11):
        print(f'o valor e {n_tabuada} x {n_tabuada * c}')