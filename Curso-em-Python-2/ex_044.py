valor_compr = int(input("Digite o Valor da sua compra"))
print('''Digite qual das opçoes Voce deseja

[1] A Vista Dinheiro/Cheque
[2] A vista no Cartão
[3] 2X no Cartão
[4] 3x ou Mais vvezes no cartão''')
desc1 =valor_compr-(valor_compr/100 * 10)
desc2 =valor_compr-(valor_compr/100 * 5)
novo_valor=valor_compr*0.2+valor_compr

opc = int(input("Qual sua Opção"))
if opc == 1:
    print("O valor de {} teve um desconto e saira por {}".format(valor_compr,desc1))
if opc == 2:
    print(" O valor de {}c{}".format(valor_compr,desc2))
if opc ==3:
    print("O valor de {} ficou em  {} foi para".format(valor_compr,valor_compr))
if opc ==4:
    parc = int(input("Quantas parcelas voce quer dividir"))
    print("O Valor de {} foi divido por {} parcelas com os juros foi para {}".format(valor_compr,parc,novo_valor))