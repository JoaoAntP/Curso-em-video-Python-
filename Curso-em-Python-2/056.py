somaidade = 0
media_idade = 0
maior_idade_homem = 0
nomevelhor = ''
q_mulher = 0
for p in range(1,3):
    print("-----{} PESSOA-----".format(p))
    nome = str(input("Digite seu nome")).strip()
    idade = int(input("Digite sua idade"))
    sexo = str(input("Sexo [M/F] :")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maior_idade_homem= idade
        nomevelhor = nome
    if sexo in 'Mn' and idade>maior_idade_homem:
        maior_idade_homem = idade
        nomevelhor = nome
    if sexo in 'Ff' and idade< 20:
        q_mulher += 1
media_idade = somaidade/4

print("A idade media foi {}".format(media_idade))
print("O homem mais velho tem {} e se chama {} ".format(maior_idade_homem, nomevelhor))
print("Ao total tem um numero de {} mulheres".format(q_mulher))