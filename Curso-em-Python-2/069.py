print("-"*30)
print("Cadastre uma Pessoa")
print("-"*30)
maior = totalH = totalM20= 0
while True:
    idade = int(input("Idade :"))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F]:")).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        totalH += 1
    if sexo == 'F' and idade < 20:
        totalM20 +=1
    print("-" * 30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Deseja continuar ? [S/N]: ")).strip().upper()[0]

    if continuar == "N":
        print(f"""
        o numero de pessoas com mais de 18 anos e: {maior}
        ao todo foram {totalH} homens cadastrados
        o total de mulheres com menos de 20 foi {totalM20}
        """)

