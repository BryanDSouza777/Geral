class Pedidos:
    def __init__(self):
        self.total = 0
        self.items = []
    def adicionarItem(self,produto,quantidade):
        self.items.append(ItemPedido(produto,quantidade))
    def obterTotal(self,):
        for i in self.items:
            self.total += i.quantidade * i.produto.valor
            return self.total
class ItemPedido:
    def __init__(self,produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
class Produto:
    def __init__(self,codigo,valor,descrição):
        self.codigo = codigo
        self.valor = valor
        self.descrição = descrição
fraldaGeriatrica = Produto('001',60,'Fralda Geriatrica')
aguaDeBanho = Produto('666',15000,'Agua Gostosas')
controle = Produto('002',20,'Controle')
pedido = Pedidos()
pedido.adicionarItem(fraldaGeriatrica,10)
pedido.adicionarItem(aguaDeBanho,2)
pedido.adicionarItem(controle,1)

print(pedido.obterTotal())
print(pedido.items[0].produto.valor)