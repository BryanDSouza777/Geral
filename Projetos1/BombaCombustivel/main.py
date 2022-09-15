from bomba import BombaCombustivel

nome = input('Digite seu nome: ')

b1 = BombaCombustivel(nome,'Gasolina',6.57,100)

def main():
    dsj = int(input('Você deseja abastecer o seu veiculo por:\n1-Valor\n2-Litros\n3-Alterar as informações da bomba\n4-Sair\n\n'))
    match dsj:
        case 1:
            valor = float(input('\nQuantos reais de combustivel deseja abastecer?\n\n'))
            b1.abastecerPorValor(valor)
        case 2:
            litros = float(input('\nQuantos litros de combustivel deseja abastecer?\n\n'))
            b1.abastecerPorLitro(litros)
        case 3:
            dsj2 = int(input('Você deseja alterar:\n1-Valor\n2-Combustivel\n3-Quantidade\n4-Sair\n\n'))
            match dsj2:
                case 1:
                    nvalor = float(input('Qual o novo valor do combustivel?\n\n'))
                    b1.alterarValor(nvalor)
                    print(f'Valor alterado para R${nvalor}')
                    main()
                case 2:
                    ncombustivel = input('Qual o novo combustivel?\n\n')
                    nvalor = float(input('Qual o novo valor do combustivel?\n\n'))
                    b1.alterarCombustivel(ncombustivel,nvalor)
                    print(f'Combustivel alterado para {ncombustivel}, e valor alterado para R${nvalor}')
                    main()
                case 3:
                    nquantidade = float(input('Qual a nova quantidade de combustivel na bomba?\n\n'))
                    b1.alterarQuantidade(nquantidade)
                    print(f'Quantidade de combustivel na bomva alterado para {nquantidade}')
                    main()
        case 4:
            exit()
        case _:
            print('Opção Inexistente')
main()