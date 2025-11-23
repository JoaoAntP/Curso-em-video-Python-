ano = int(input("Diga o ano que voce deseja saber se foi bissexto ou não :"))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0 :
    print("Sim {} foi bissexto".format(ano))
else:
    print(" {} não foi bissexto ".format(ano))