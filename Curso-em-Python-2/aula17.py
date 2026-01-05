"""lista = [8,2,9,1,7,3,3,4,4]
#append(add na ultima posição)
#insert
#del/pop(ultimo elemento)/remove(pelo nome)(remover)
valores = list(range(4,13))
print( valores)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
print(len(lista))
lista.append(4)
print(lista)
lista.insert(2, 0)
print(lista)
lista.pop()
print(lista)
if 4 in lista:
    lista.remove(4)
print(lista)"""


#valores = []
#valores.append(9)
#valores.append(5)
#valores.append(3)

#for c, v in enumerate(valores):
    #print(f'Na  posição {c} encontrei o valor {v}')

a = [4,7,6,-2]
b = a[:]
b[3] = 2
print(b)