class Quadrado:
    def __init__(self,tamanho):
        self.tamanho = float(tamanho)
    def mudarLado(self,mlado):
        self.tamanho = mlado
    def calcular(self):
        return self.tamanho **2