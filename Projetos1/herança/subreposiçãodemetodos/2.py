class Mamifero():
    def __init__(self,nome,peso,cor):
        self.nome = nome
        self.peso = peso
        self.cor = cor
    def locomoção(self):
        print(f'{self.nome} caminha')
    def comunicação(self,animal):
        print(f'{self.nome} está se comunicando por latidos com {animal}')
    def alimentação(self):
        print(f'{self.nome} se alimenta de Ração')
    def habitatNatural(self):
        print(f'{self.nome} vive em casa')
    def mostraTudo(self):
        print(f'Locomoção: {self.locomoção()}\nComunicação: {self.comunicação()}\nAlimentação: {self.alimentação()}\nHabitat Natural: {self.habitatNatural()}')

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    def comunicação(self,animal):
        print(f'{gato.nome} está se comunicando por miados com {animal}')
    pass

class Baleia(Mamifero):
    def locomoção(self):
        print(f'{baleia.nome} nadando')
    def comunicação(self,animal):
        print(f'{baleia.nome} está se comunicando por baleiês com {animal}')
    def alimentação(self):
        print(f'{self.nome} se alimenta de Peixe')
    def habitatNatural(self):
        print(f'{baleia.nome} vive no Mar')

class Macaco(Mamifero):
    def locomoção(self):
        print(f'{macaco.nome} pulando sobre galhos')
        return 'Pulando sobre galhos'
    def comunicação(self,animal):
        print(f'{macaco.nome} está se comunicando por gritos com {animal}')
        return 'Gritos'
    def alimentação(self):
        print(f'{self.nome} se alimenta de Banana')
        return 'Banana'
    def habitatNatural(self):
        print(f'{macaco.nome} vive na Floresta')
        return 'Floresta'
    def mostraTudo(self):
        print(f'Locomoção: {self.locomoção()}\nComunicação: {self.comunicação(baleia)}\nAlimentação: {self.alimentação()}\nHabitat Natural: {self.habitatNatural()}')

macaco = Macaco('Jorge',3.5,'Marrom')
gato = Gato('Alfred',4.5,'Amarelo')
cachorro = Cachorro('tobby',5,'pretin')
baleia = Baleia('famosa mãe do renan',5000000,'azul')

macaco.mostraTudo()