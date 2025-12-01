n = 0
soma= k = 0
while True:
    n = int(input("Digite um numero [999 faz parar] :"))
    if n == 999:
        break
    k += 1
    soma += n
print(f'A quantidade de numero digitados foi {k} e a soma deles foi {soma}')