n1 = float(input('Digite um Numero \n \n'))

n2 = float(input('\nDigite outro Numero \n \n'))

n3 = float(input('\nDigite mais um Numero \n \n'))

if n1 > n2 and n1 > n3:
    print ('\n Maior numero é:',n1)

elif n2 > n1 and n2 > n3:
    print ('\n Maior numero é:',n2)

elif n3 > n1 and n3 > n2:
    print ('\n Maior numero é:',n3)

if n1 < n2 and n1 < n3:
    print ('\n Menor numero é:',n1)

elif n2 < n1 and n2 < n3:
    print ('\n Menor numero é:',n2)

elif n3 < n1 and n3 < n2:
    print ('\n Menor numero é:',n3)