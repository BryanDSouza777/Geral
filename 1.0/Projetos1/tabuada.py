while True:

    tabuada = float(input('Digite um numero para ver a tabuada\n\n'))
    if tabuada == 0:
        print('Encerrando...')
        break
    elif tabuada != 0:
        y = int(input('Digite até qual numero será multiplicado'))
        print ("\nTabuada do",int(tabuada),'\n')
        for i in range(0,y+1):
            print(tabuada*i)
        print('\nContinuando...')
    else:
        exit()
