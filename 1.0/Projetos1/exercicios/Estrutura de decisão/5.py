n1 = float(input('Digite sua primeira nota\n\n'))
n2 = float(input('\nDigite sua segunda nota\n\n'))
n3 = float(input('\nDigite sua terceira nota\n\n'))
n4 = float(input('\nDigite sua quarta nota\n\n'))

media = ((n1 + n2 +n3 +n4)/4)
print ('\n',media,'\n')

if media >= 7:
    print('Aprovado')

elif media < 7:
    print('Reprovado')

elif media == 10:
    print('Aprovado com Distinção')