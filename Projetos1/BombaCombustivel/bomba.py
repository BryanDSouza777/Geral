class BombaCombustivel:
    def __init__(self,nome,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.nome = nome
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self,valor):
        litros = (valor / self.valorLitro)
        if litros > self.quantidadeCombustivel:
            print('Não foi possivel abastecer.\nFaltou combustivel na bomba.')
        else:
            self.quantidadeCombustivel -= litros
            print(f'Você abasteceu R${valor:.2f} de {self.tipoCombustivel} ({litros:.2f} Litros)')

    def abastecerPorLitro(self,litros):
        if litros > self.quantidadeCombustivel:
            print('Não foi possivel abastecer.\nFaltou combustivel na bomba.')
        else:
            valor = litros * self.valorLitro
            print(f'Você abasteceu R${valor:.2f} de {self.tipoCombustivel} ({litros:.2f} Litros)')

    def alterarValor(self,valor):
        self.valorLitro = valor
        print(f'Valor alterado para {valor}')

    def alterarCombustivel(self,combustivel,valor):
        self.tipoCombustivel = combustivel
        self.valorLitro = valor
        print(f'Combustivel alterado para {combustivel}\nValor alterado para {valor}')

    def alterarQuantidade(self,quantidade):
        self.quantidadeCombustivel = quantidade
        print(f'Quantidade de combustivel alterado para {quantidade}')