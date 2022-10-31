from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self):
        pass
class B(A):
    def falar(self):
        print('Falando...B')

b = B()
b.falar()