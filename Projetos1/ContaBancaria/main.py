from a import ContaEspecial,ContaPoupança

opc = int(input('Qual conta deseja criar?\n1-Conta Especial\n2-Conta Poupança\n3-Sair\n'))
nome = input('\nQual o seu nome?\n\n')
match opc:
    case 1:
        cliente = ContaEspecial(nome,148072,0,500)
        print(cliente.saldo)
        dinheiro = float(input('Quanto deseja depositar?'))
        cliente.depositar(dinheiro)
        print(cliente.saldo)
        dinheiro = float(input('Quanto deseja sacar?'))
        cliente.sacar(dinheiro)
        print(cliente.saldo)
    case 2:
        cliente = ContaPoupança(nome,151012,0,10)
        print(cliente.saldo)
        dinheiro = float(input('Quanto deseja depositar?'))
        cliente.depositar(dinheiro)
        print(cliente.saldo)
        dinheiro = float(input('Quanto deseja sacar?'))
        cliente.sacar(dinheiro)
        print(cliente.saldo)
        cliente.calcularNovoSaldo()
        print('Poupança rendendo')
        print(cliente.saldo)
    case 3:
        exit()
    case _:
        print('Opção Inválida')