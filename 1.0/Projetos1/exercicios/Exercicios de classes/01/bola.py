class Bola:
    def __init__(self,cor,material,circunferencia):
        self.cor = cor
        self.material = material
        self.circun = circunferencia
    def trocaCor(self,corNova):
        self.cor = corNova
    def mostrarCor(self):
        print(self.cor)