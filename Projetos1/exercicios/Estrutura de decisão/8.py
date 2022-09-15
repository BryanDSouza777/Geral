p1 = float(input('Digite o preço do primeiro produto \n \n'))

p2 = float(input('\nDigite o preço do segundo produto \n \n'))

p3 = float(input('\nDigite o preço do terceiro produto \n \n'))

if p1 < p2 and p1 < p3:
    print ('\nCompre o primeiro produto.\nValor R$',p1)

elif p2 < p1 and p2 < p3:
    print ('\nCompre o segundo produto.\nValor R$',p2)

elif p3 < p1 and p3 < p2:
    print ('\nCompre o terceiro produto.\nValor R$',p3)