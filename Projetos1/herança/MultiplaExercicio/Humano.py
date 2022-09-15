class Humano:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def jogarVava(self):
        print(f'{self.nome} jogando Valorant.')
class Inseto:
    def __init__(self,nomein,veneno,alado):
        self.nomein = nomein
        self.veneno = veneno
        self.alado = alado
    def caçando(self):
        print(f'{self.nomein} foi procurar comida para o jantar.')
class SuperHeroi(Humano,Inseto):
    def __init__(self,humano,inseto):
        super().__init__(humano.nome,humano.idade)
        Inseto.__init__(self,inseto.nomein,inseto.veneno,inseto.alado)
        self.nomein = inseto.nomein
        self.codinome = humano.nome +'-'+ self.nomein
        self.poderes = []
    def salvandoVidas(self):
        print(f'{self.codinome} salvou uma pessoa de um acidente.')
barata = Inseto('Barata',False,True)
humano = Humano('Enma',16)
LucasArt = SuperHeroi(humano,barata)
LucasArt.jogarVava()
LucasArt.caçando()
LucasArt.salvandoVidas()
