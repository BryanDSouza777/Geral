def faixa_etaria (lista):
    fx1=[]
    fx2=[]
    fx3=[]
    fx4=[]
    fx5=[]
    for i in range(len(lista)):
        if lista[i] <= 15:
            fx1.append(lista[i])
        elif lista[i] >= 16 and lista[i] <= 30:
            fx2.append(lista[i])
        elif lista[i] >= 31 and lista[i] <= 45:
            fx3.append(lista[i])
        elif lista[i] >= 46 and lista[i] <= 60:
            fx4.append(lista[i])
        elif lista[i] >= 61:
            fx5.append(lista[i])

    print (f'{len(fx1)} pessoas do teste estão na faixa etária de Até 15 anos.\n')
    print (f'{len(fx2)} pessoas do teste estão na faixa etária de 16 à 30 anos.\n')
    print (f'{len(fx3)} pessoas do teste estão na faixa etária de 31 à 45 anos.\n')
    print (f'{len(fx4)} pessoas do teste estão na faixa etária de 46 à 60 anos.\n')
    print (f'{len(fx5)} pessoas do teste estão na faixa etária de acima de 61 anos.\n')

    print (f'{(100*len(fx1)/15):.2f}% das pessoas do teste estão na faixa etária de Até 15 anos\n')
    print (f'{(100*len(fx5)/15):.2f}% das pessoas do teste estão na faixa etária de Acima de 61 anos')

idade = [15, 16, 17, 19, 30, 67, 7, 9, 72, 49, 80, 15, 16, 41, 14]
faixa_etaria (idade)