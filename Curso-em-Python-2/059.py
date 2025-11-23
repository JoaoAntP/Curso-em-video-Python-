v1 = 0
v2 = 0
opcao = 0

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor valor: "))

while opcao != 5:
    print('''Qual opção você deseja selecionar

    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
''')

    opcao = int(input("Qual opção você deseja selecionar"))
    if opcao == 1:
            soma = v1+v2
            print(" O resultado e {}".format(soma))
    elif opcao == 2:
            multi = v1 * v2
            print(" O resultado e {}".format(multi))
    elif opcao == 3:
        if v1>v2:
            print("O numero 1 e maior que o numero 2")
        elif v1< v2:
            print("O numero 2 e maior que o numero 1")
    elif opcao == 4:
            print(" Informe novamente seus numeros")
            v1 = int(input("Digite o primeiro valor: "))
            v2 = int(input("Digite o segundo valor valor: "))
    elif opcao == 5:
            print(" Finalizando...")
    else:
         print("Erro, Opção Invalida")
    print("=-="*10)
print("Fim do programa")