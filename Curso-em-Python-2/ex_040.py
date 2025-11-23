nota1 = float(input("Digite o valor da sua nota"))
nota2 = float(input("Digite o valor da sua nota"))
media = nota1+nota2/2
if media >= 0 and media <2 :
    print("Infelizmente sua media foi muito ruim Reprovado")
elif media >= 3 and media <4:
    print("Infelizmente sua media foi ruim Reprovado")
elif media >= 5 and media <6:
    print("Voce passou")
elif media >= 7 and media <8:
    print("Muito bem")
else:
    print("Impeccavel")