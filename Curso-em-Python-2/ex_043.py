altu = float(input("Digite sua altura :"))
peso = float(input('Digite seu peso :'))
IMC = peso/(altu**2)
print("seu IMC e  de {}".format(IMC))
if  IMC < 18.5:
    print(" Esta Abaixo ")
elif  18.5<= IMC < 25:
    print(" Esta Ideal ")
elif 25<= IMC < 30:
    print(" Esta Acima do peso ")
elif 30<= IMC < 40:
    print("Esta Obesidade ")
else:
    print("Voce esta com obesidade Morbida")
