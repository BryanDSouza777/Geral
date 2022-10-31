sexo = str(input("Digite seu sexo\nM = Masculino\nF = Feminino\n\n"))
Masculino = ['Masculino','masculino','m','MASCULINO','M']
Feminino = ['Feminino','feminino','f','FEMININO','F']

if sexo in Masculino:
    print ("\nVocê é do sexo",Masculino[0])

elif sexo in Feminino:
    print ("\nVocê é do sexo",Feminino[0])

else:
    print("\nSexo Inválido")