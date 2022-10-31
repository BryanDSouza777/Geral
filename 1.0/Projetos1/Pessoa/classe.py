class Pessoa:
    def __init__(self,nome):
        self.nome = nome
        self.__vida = 100
        self.__energia = 100
        self.__mana = 70
        self.__fome = 100

    @property
    def energia(self):
        return self.__energia
    @energia.setter
    def energia(self,valor):
        self.__energia = valor

    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self,valor):
        self.__vida = valor

    @property
    def mana(self):
        return self.__mana
    @mana.setter
    def mana(self,valor):
        self.__mana = valor

    @property
    def fome(self):
        return self.__fome
    @fome.setter
    def fome(self,valor):
        self.__fome = valor

    def soltarFeitiço(self,feitiço,valor):
        self.mana -= valor
        print(self.nome,"Soltou",feitiço)

    def PerderVida(self,valor):
        self.vida+=valor

p = Pessoa('Enma')
p.energia = 150
print(p.energia)
p.energia -= 1
print(p.energia)
print(p.mana)
p.soltarFeitiço('FullCounter',30)
print(p.mana)