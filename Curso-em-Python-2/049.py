nt = int(input("Digite o numero que deseja fazer a tabuada"))
for c in range(0, 11):
    tabuada = nt*c
    print("{} x {:2} = {}".format(nt, c, tabuada))