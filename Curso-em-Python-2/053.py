frase = str(input("Digite uma frase ")).strip().upper()
palavras = frase.split()
tdjunto = '' .join(palavras)
inverso =tdjunto[:: -1]
#for c in range(len(tdjunto) -1, -1, -1):
    #inverso += tdjunto[letra]
print(tdjunto, inverso)
if inverso == tdjunto:
    print("Temos um palindrome")
else:
    print("Não e um palindromo")