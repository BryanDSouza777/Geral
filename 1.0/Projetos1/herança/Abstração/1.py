from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def falar(self):
        pass
class B(A):
    def falar(self):
        print('oi')
b = B()
b.falar()