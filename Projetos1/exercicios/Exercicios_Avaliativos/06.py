#6.O código a seguir está certo?Se não estiver,como você iria resolver e qual é o problema.
# i = 0
# while i < 10:
#   print(i)
#   if i == 7:
#       break

'''Resposta'''
#Se não colocar algo para aumentar o valor do "i" ele ficará num loop para sempre, entao no final do loop, fora da área
#do "If" ou antes do "If", colocar um (i += 1)

#exemplo
'''
i = 0
while i < 10:
    print(i)
    i += 1
    if i == 7:
        break
'''