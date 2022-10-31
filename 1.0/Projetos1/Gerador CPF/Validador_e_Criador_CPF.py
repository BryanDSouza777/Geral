import random
while True:
    djs = input("Você deseja Criar um CPF valido(1) ou verificar a validação do seu CPF(2)?\n\n")

    def UltimosDigitos(lista):

        m1 = []
        for e in range(9):  
            m1.append(int(lista[e]) * (10 - e))
        mt1 = (sum(m1) * 10) % 11
        if mt1 >= 10:
            mt1 = 0
        lista += str(mt1)

        m2 = []
        for a in range(10):
            m2.append(int(lista[a]) * (11 - a))
        mt2 = (sum(m2)* 10) % 11
        if mt2 >= 10:
            mt2 = 0
        lista += str(mt2)

        cpf = (f'\n{lista[0]}{lista[1]}{lista[2]}.{lista[3]}{lista[4]}{lista[5]}.{lista[6]}{lista[7]}{lista[8]}-{lista[9]}{lista[10]}')
        print (cpf)
        if djs == '1':
            print(' ')
        elif djs == '2':
            if seucpf[9] == str(mt1) and seucpf[10] == str(mt2):
                print('\nCPF Válido!')
            elif seucpf[9] != str(mt1) or seucpf[10] != str(mt2):
                print('\nCPF Inválido')

    if djs != '1' and djs != '2':
        print('\nDigite apenas "1" ou "2"!\n')#anti quebra
        continue
    elif djs == '1':
        n1 = []
        for i in range(9):
            nr = random.randint(0,9)#numeros aleatorios
            n1.append(nr)

        UltimosDigitos (n1)
        break

    elif djs == '2':
        while True:
            try:
                seucpf = (input("Digite seu CPF\n\n"))
            except:
                print('CPF não pode conter letras ou sinais, apenas números')
            if str(seucpf) == str(seucpf)[::-1]:#anti falsa validação
                print('CPF com caracteres repetidos é inválido!')
                continue
            else:
                break
            
        if len(str(seucpf)) != 11:
            print ("\nCPF está incorreto, digite sem '.' e '-'")
            continue
        UltimosDigitos(seucpf)
    break 