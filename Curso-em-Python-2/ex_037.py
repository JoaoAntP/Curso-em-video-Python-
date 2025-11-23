num = int(input("Digite um numero"))
print('''Digite para qual opçao voce deseja converter seu numero:"
          "[1] Binario"
          "[2] Octal"
          "[3] Hexadecimal''')
opcao = int(input("Digite a sua opção :"))
if opcao == 1:
    print("o resultado de {} e numero {}".format(num,bin(num)))
elif opcao == 2:
    print("o resultado de {} e numero {}".format(num,oct(num)))
elif opcao == 3:
    print("o resultado de {} e numero {}".format(num,hex(num)))
else:
    print("Opção invalida")