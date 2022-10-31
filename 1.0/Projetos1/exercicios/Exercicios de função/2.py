valor = []

def nesima(n):

    for i in range(1,n+1): #para 9 elementos
        if i < 10:

            valor.append(i)
            print(valor)
x = int(input("Digite um numero."))
nesima(x)
