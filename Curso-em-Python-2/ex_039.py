from datetime import date
data_nasc = int(input("Em qual ano voce nasceu"))
idade =  date.today().year - data_nasc
data_alistamento = data_nasc+18
tempo_falta =  data_alistamento - data_nasc - idade
ano_alist= data_nasc+18

quant_tempo = data_alistamento-date.today().year
if data_alistamento==0 :
    print("Este e o ano do seu alistamento voce tem {}".format(idade))
elif idade < 18:
    print("Ainda faltam {} anos para voce se inscrever se prepare voce tem {}".format(tempo_falta,idade))
else:
    print("Ja passou sua data de inscrição foi quando voce tinha {},{}".format(ano_alist,quant_tempo))