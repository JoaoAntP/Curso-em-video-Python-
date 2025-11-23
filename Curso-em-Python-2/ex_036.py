valor_casa = float(input("Digite o valor da Casa que voce deseja comprar : "))
salar = float(input("Digite seu salario : "))
parcela = int(input('Em quantas parcelas voce deseja parcelar :'))
valor_parcelas = valor_casa/parcela
porc_salar = salar%30
if  porc_salar>=valor_parcelas:
    print("Parabens Compra aprovada")
else:
    print("Infelizmente não podemos aprovar a compra tente depois")