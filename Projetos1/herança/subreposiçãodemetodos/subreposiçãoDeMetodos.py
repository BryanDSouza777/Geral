from mimetypes import init


class Mamifero():
    def __init__(self,nome,peso,cor,barulho):
        self.nome = nome
        self.peso = peso
        self.cor = cor
        self.barulho = barulho
    def locomoção(self):
        print(f'{self.nome} caminha')
    def comunicação(self,animal):
        print(f'{self.nome} está se comunicando por {self.barulho} com {animal.nome}')
    def alimentação(self):
        pass
    def habitatNatural(self):
        pass
class Cachorro(Mamifero):
    pass
class Gato(Mamifero):
    pass
class Baleia(Mamifero):
    pass
class Macaco(Mamifero):
    pass

macaco = Macaco('Jorge',3.5,'Marrom','grito')
gato = Gato('Alfred',4.5,'Amarelo','miado')
cachorro = Cachorro('tobby',5,'pretin','latido')
baleia = Baleia('A famosa mãe do renan',5000000,'azul','baleiês')
conversando = 'cachorro'

macaco.locomoção()
macaco.comunicação(baleia)
gato.comunicação(baleia)
cachorro.comunicação(baleia)
baleia.comunicação(macaco)