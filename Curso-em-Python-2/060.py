n_fat = int(input("Digite um número para que possamos calcular seu Fatorial :"))
c = n_fat
f = 1
print('calculando {}! ='.format(n_fat), end='')
while c > 0:
    print("{}".format(c), end='')
    print(' x ' if c > 1 else ' = ', end='' )
    f *= c
    c -=1
    print('{}'.format(f))