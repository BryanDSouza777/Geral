from abc import ABC, abstractmethod
from calendar import c
class FormaGeometrica(ABC):
    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Quadrado(FormaGeometrica):
    def __init__(self,lado):
        self.lado = lado
    def perimetro(self):
        return self.lado*4
    def area(self):
        return self.lado ** 2
class Triangulo(FormaGeometrica):
    def __init__(self,base,ladoA,altura):
        self.base = base
        self.ladoA = ladoA
        self.altura = altura
    def area(self):
        return (self.base * self.altura)/2
    def perimetro(self):
        return (self.base + self.ladoA + self.altura)
class Circulo(FormaGeometrica):
    def __init__(self,raio) -> None:
        self.raio = raio
        self.pi = 3.1415
    def area(self):
        return self.pi*(self.raio**2)
    def perimetro(self):
        return 2*self.pi*self.raio
class Pentagono(FormaGeometrica):
    def __init__(self,lado,apotema) -> None:
        self.lado = lado
        self.apotema = apotema
    def area(self):
        return (5*self.lado*self.apotema)/2
    def perimetro(self):
        return self.lado*5
q = Quadrado(3)
t = Triangulo(3,4,5)
c = Circulo(5)
p = Pentagono(5,3)

print('Quadrado:\n')
print(f'{q.perimetro():.2f}')
print(f'{q.area():.2f}')
print('Triangulo:\n')
print(f'{t.perimetro():.2f}')
print(f'{t.area():.2f}')
print('Circulo:\n')
print(f'{c.perimetro():.2f}')
print(f'{c.area():.2f}')
print('Pentagono:\n')
print(f'{p.perimetro():.2f}')
print(f'{p.area():.2f}')