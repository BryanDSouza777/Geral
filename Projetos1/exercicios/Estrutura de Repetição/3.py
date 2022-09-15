while True:
    nome = str(input("Digite seu nome\n"))
    if len(nome) < 3:
        print("Seu nome dele ter mais de 3 letras")
        continue
    
    else:
        break

while True:

    idade = int(input("\nDigite sua idade\n\n"))
    if idade <= 0 and idade > 150:
        print("\nIdade inválida\n")
        continue

    else:
        break

while True:
    salario = float(input("\nDigite seu salário\n\n"))
    if salario < 1:
        print("\nSalário inexistente\n")
        continue
    
    else:
        break

while True:
    sexo = str(input("\nDigite seu sexo\nm = masculino\nf = feminino\n\n"))
    sexo = sexo.lower()
    if sexo != 'm' and sexo != 'f':
        print("Sexo Inválido")
        continue

    else:
        break

while True:
    estadocivil = str(input("\nDigite seu Estado Civil\ns = solteiro(a)\nc = casado(a)\nv = viúvo(a)\nd = Divorciado(a)\n\n").lower)
    if sexo == 's' or 'c' or 'v' or 'd':
        print("\nEstado Civil inválido")
        continue

    else:
        break

x = 1
while x == 1:
    print(f'\nSeu nome é {nome}')
    print(f'\nVocê tem {idade} anos de idade\n')
    print(f'\nSeu salário é de R$ {salario}\n')

    if sexo == 'm':
        print("\nVocê é do sexo Masculino\n")
    elif sexo == 'f':
        print("\nVocê é do sexo Feminino\n")

    if estadocivil == 's':
        print("\nVocê está solteiro(a)")
        break
    elif estadocivil == 'c':
        print("\nVocê está casado(a)")
        break
    elif estadocivil == 'v':
        print("\nVocê está viúvo(a)")
        break
    elif estadocivil == 'd':
        print("\nVocê está divorciado(a)")
        break

    x += 1
