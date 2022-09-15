class Pessoa:
    def __init__(self, nome, idade, altura, falando = False, comendo = False):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.falando = falando
        self.comendo = comendo
    def estaComendo(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja está comendo.')
            return
        if self.falando:
            print(f'{self.nome} não pode comer pois está falando.')
        print(f'{self.nome} está comendo {alimento}')

