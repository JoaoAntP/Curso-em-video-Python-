from datetime import date
data_nasc = int(input("Em qual ano voce nasceu"))
idade =  date.today().year - data_nasc
if idade <= 7:
    print('Voce e mirin')
elif idade <= 14:
    print("Voce e dda categoria infantil")
elif idade <= 19:
    print("Voce Junior")
elif idade <= 25:
    print("Voce e senior")
else:
    print("Master")