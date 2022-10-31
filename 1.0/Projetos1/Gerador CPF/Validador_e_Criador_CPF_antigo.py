import random

while True:
    djs = input("Você deseja Criar um CPF valido(1) ou verificar a validação do seu CPF(2)?\n\n")

    if djs != '1' and djs != '2':
        print('\nDigite apenas "1" ou "2"!\n')#anti quebra
        continue

    elif djs == '1':
        while True:
            n1 = random.randint(0,9)#numeros aleatorios
            n2 = random.randint(0,9)
            n3 = random.randint(0,9)
            n4 = random.randint(0,9)
            n5 = random.randint(0,9)
            n6 = random.randint(0,9)
            n7 = random.randint(0,9)
            n8 = random.randint(0,9)
            n9 = random.randint(0,9)

            cpf = (f'{n1}{n2}{n3}.{n4}{n5}{n6}.{n7}{n8}{n9}-')
            CpfDg1 = n1 * 10#Digitos do CPF
            CpfDg2 = n2 * 9
            CpfDg3 = n3 * 8
            CpfDg4 = n4 * 7
            CpfDg5 = n5 * 6
            CpfDg6 = n6 * 5
            CpfDg7 = n7 * 4
            CpfDg8 = n8 * 3
            CpfDg9 = n9 * 2
            x = (CpfDg1 + CpfDg2 + CpfDg3 + CpfDg4 + CpfDg5 + CpfDg6 + CpfDg7 + CpfDg8 + CpfDg9)#soma
            CpfDg10 = (x * 10) % 11#validação
            if CpfDg10 >= 10:
                CpfDg10 = 0

            CpfDg01 = n1 * 11#Digitos do CPF Também, multiplicaçãp
            CpfDg02 = n2 * 10
            CpfDg03 = n3 * 9
            CpfDg04 = n4 * 8
            CpfDg05 = n5 * 7
            CpfDg06 = n6 * 6
            CpfDg07 = n7 * 5
            CpfDg08 = n8 * 4
            CpfDg09 = n9 * 3
            CpfDg010 = CpfDg10 * 2
            y = (CpfDg01 + CpfDg02 + CpfDg03 + CpfDg04 + CpfDg05 + CpfDg06 + CpfDg07 + CpfDg08 + CpfDg09 + CpfDg010)#soma
            CpfDg011 = (y * 10) % 11#validação
            if CpfDg011 >= 10:
                CpfDg011 = 0
            print (f'\n{cpf}{CpfDg10}{CpfDg011}') #imprimir cpf aleatorio com a chave válida   
            break
        break


    elif djs == '2':
        while True:
            #111 111 111 11
            #012 345 678 91
            y = 1
            while True:
                try:
                    seucpf = int(input("Digite seu CPF\n\n"))
                except:
                    print('CPF não pode conter letras ou sinais, apenas números')
                    continue
                if str(seucpf) == str(seucpf)[::-1]:#anti falsa validação
                    print('CPF com caracteres repetidos é inválido!')
                    continue
                else:
                    break

            z1 = (str(seucpf)[0])#atalho para digito especifico do cpf
            z2 = (str(seucpf)[1])#(variable) int
            z3 = (str(seucpf)[2])
            z4 = (str(seucpf)[3])
            z5 = (str(seucpf)[4])
            z6 = (str(seucpf)[5])
            z7 = (str(seucpf)[6])
            z8 = (str(seucpf)[7])
            z9 = (str(seucpf)[8])
            z10 = (str(seucpf)[9])
            z11 = (str(seucpf)[10])

            if len(str(seucpf)) != 11:
                print ("\nCPF está incorreto, digite sem '.' e '-'")
                continue
            else:
                dg1 = int(z1) * 10#digito cpf, multiplicação
                dg2 = int(z2) * 9
                dg3 = int(z3) * 8
                dg4 = int(z4) * 7
                dg5 = int(z5) * 6
                dg6 = int(z6) * 5
                dg7 = int(z7) * 4
                dg8 = int(z8) * 3
                dg9 = int(z9) * 2
                a = (dg1 + dg2 + dg3 + dg4 + dg5 + dg6 + dg7 + dg8 + dg9)#soma
                dg10 = ((a * 10) % 11) % 10#validação
                if dg10 > 9:
                    dg10 = 0

                dg01 = int(z1) * 11#outros digitos cpf, multiplicação
                dg02 = int(z2) * 10
                dg03 = int(z3) * 9
                dg04 = int(z4) * 8
                dg05 = int(z5) * 7
                dg06 = int(z6) * 6
                dg07 = int(z7) * 5
                dg08 = int(z8) * 4
                dg09 = int(z9) * 3
                dg010 = int(dg10) * 2
                b = int(dg01 + dg02 + dg03 + dg04 + dg05 + dg06 + dg07 + dg08 + dg09 + dg010)#soma
                dg011 = ((b * 10) % 11) % 10#validação
                if dg011 > 9:
                    dg011 = 0
                
                if int(z10) != dg10 or int(z11) != dg011:
                    print('\nCPF Inválido\n\nTente outro!\n')
                    continue

                elif int(z10) == dg10 and int(z11) == dg011:
                    print (f'\n{str(seucpf)[0:3]}.{str(seucpf)[3:6]}.{str(seucpf)[6:9]}-{str(dg10)}{str(dg011)}')
                    print("\nCPF Válido")
                    break
                break
    break