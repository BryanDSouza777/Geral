import random
# Construa um algoritmo de maneira que ele imprima
# o percentual de pessoas considerando as faixas de idade:
# 0-17anos,18a34anos,35a49anos,50a64 anos e maiores de 64 anos.
# Lembrete:a soma dos percentuais das faixas deve totalizar 100%
def faixa_etaria (lista):
    fx1=[]
    fx2=[]
    fx3=[]
    fx4=[]
    fx5=[]
    for i in range(len(lista)):
        if lista[i] < 18:
            fx1.append(lista[i])
        elif lista[i] > 17 and lista[i] < 35:
            fx2.append(lista[i])
        elif lista[i] > 34 and lista[i] < 50:
            fx3.append(lista[i])
        elif lista[i] > 49 and lista[i] < 65:
            fx4.append(lista[i])
        elif lista[i] > 64:
            fx5.append(lista[i])

    print (f'{len(fx1)} pessoas do teste estão na faixa etária de Até 15 anos.\n')
    print (f'{len(fx2)} pessoas do teste estão na faixa etária de 16 à 30 anos.\n')
    print (f'{len(fx3)} pessoas do teste estão na faixa etária de 31 à 45 anos.\n')
    print (f'{len(fx4)} pessoas do teste estão na faixa etária de 46 à 60 anos.\n')
    print (f'{len(fx5)} pessoas do teste estão na faixa etária de acima de 61 anos.\n')

    print (f'{(100*len(fx1)/14):.2f}% das pessoas do teste estão na faixa etária de Até 17 anos.')
    print (f'{(100*len(fx2)/14):.2f}% das pessoas do teste estão na faixa etária de 18 à 34 anos.')
    print (f'{(100*len(fx3)/14):.2f}% das pessoas do teste estão na faixa etária de 35 à 49 anos.')
    print (f'{(100*len(fx4)/14):.2f}% das pessoas do teste estão na faixa etária de 50 à 64 anos.')
    print (f'{(100*len(fx5)/14):.2f}% das pessoas do teste estão na faixa etária de Acima de 65 anos.')

idade = []
for i in range(14):
    x = random.randint(1,150)
    idade.append(x)  
faixa_etaria (idade)