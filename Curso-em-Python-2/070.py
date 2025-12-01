print("-"*30)
print("  LOJA SUPER BARATÃO ")
print("-"*30)
total_comp =cont= menor = maiorq_mil = 0
barato= ' '
while True:
    nm_prod = str(input("Nome do Produto : "))
    preco_pro= int(input("Preço R$ : "))
    cont += 1
    total_comp+=preco_pro
    if preco_pro > 1000:
        maiorq_mil += 1
    if cont == 1:
        menor = preco_pro
        barato = nm_prod
    else:
        if preco_pro<menor:
            menor = preco_pro
            barato = nm_prod
    continuar =' '
    while continuar not in 'SN':
        continuar = str(input("Deseja continuar [S/N] :")).strip().upper()[0]
    if continuar == 'N':
        break
print("-"*20+'Fim do programa'+"-"*20)
print(f"""
O total da compra foi R$: {total_comp}
Temos {maiorq_mil} produtos custando mais de R$: 1.000
O produto mais barato foi {barato} que custo R$: {menor}        
""")