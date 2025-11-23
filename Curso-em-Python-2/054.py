from datetime import  date
atual = date.today().year
qmaior = 0
qmenor = 0
for pess in range(1,6):
    nasc = int(input("Digite a {} da primeira pessoa".format(pess)))
    idade = atual-nasc
    if idade >= 18:
        qmaior += 1
    else:
        qmenor += 1
print("Numero total de maiores de idade e {} e de menores de idade e {}".format(qmaior, qmenor))