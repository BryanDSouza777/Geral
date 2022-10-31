def reset():
    vi = float(input("Digite um Valor.\n\n"))
    pi = float(input("\nDigite a porcentagem que sera aplicada.\n\n"))
    op = (input("\nA porcentagem que sera aplicada sera\n+ = Crescente\n- = Decrescente\n\n"))

    positivo = float(vi*(1 +(pi/100)))
    negativo = float(vi*(1 -(pi/100)))
    if (op == '+'):
        print(f'\nSeu novo valor é: R$ {positivo:.2f}, com o valor de R$" {positivo - vi} acrescentado')
    elif (op == '-'):
        print(f'\nSeu novo valor é: R$ {negativo:.2f}, com o valor de R$ {negativo - vi} descontado')
    else:
        print("\nVocê digitou algo errado!")
    
    restart = (input("\nDigite '1' para reiniciar\n\n")).lower()
    if restart == ("1"):
        print("\nReiniciando...\n")
        reset()
    else:
        exit()
reset()