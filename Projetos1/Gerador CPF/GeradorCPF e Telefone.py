import random


n1 = []
for i in range(9):
    nr = random.randint(0,9)
    n1.append(nr)


def CPFAleatorio(lista):

    m1 = []
    for e in range(9):  
        m1.append(int(lista[e]) * (10 - e))
    mt1 = (sum(m1) * 10) % 11
    if mt1 >= 10:
        mt1 = 0
    lista += str(mt1)

    m2 = []
    for a in range(10):
        m2.append(int(lista[a]) * (11 - a))
    mt2 = (sum(m2)* 10) % 11
    if mt2 >= 10:
        mt2 = 0
    lista += str(mt2)

    cpf = (f'{lista[0]}{lista[1]}{lista[2]}{lista[3]}{lista[4]}{lista[5]}{lista[6]}{lista[7]}{lista[8]}{lista[9]}{lista[10]}')
    return cpf
        

CPFAleatorio(n1)



def numeroAleatorio():
    n2 = []
    for i in range(9):
        na = random.randint(0,9)
        n2.append(na)
    telefone = (f'{n2[0]}{n2[1]}{n2[2]}{n2[3]}{n2[4]}{n2[5]}{n2[6]}{n2[7]}{n2[8]}')
    return telefone