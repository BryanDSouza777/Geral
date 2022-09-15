qtd = int(input("quantas repetiçoes fibonacci\n\n"))
lista = []
for i in range(qtd):
    if i == 0:
        lista.append(0)
    elif i == 1:
        lista.append(1)
    else:
        lista.append(lista[i-2]+ lista[i-1])

print(lista)