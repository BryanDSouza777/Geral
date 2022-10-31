vogais: ["a","e","i","o","u"]

while True:
    vetor = str(input("Digite uma palavra com 10 caracteres."))
    vetor = vetor.lower()

    if len(vetor) != 10:
        print("Esta palavra não tem 10 caracteres.")
        continue

    elif len(vetor) == 10:
        lista = list(vetor)
        print (lista)
        len(list) == vogais
        break


    