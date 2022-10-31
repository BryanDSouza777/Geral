class A:
    def falar(self):
        print('Falando...A')


class B(A):
    def falar(self):
        print('Falando...B')
    def saudação(self):
        print('Oi')

class C(A):
    def falar(self):
        print('Falando...C')


class D(B,C):
    pass

d = D()
d.falar()
d.saudação()