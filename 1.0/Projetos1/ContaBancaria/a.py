from abc import ABC, abstractmethod
class ContaBancaria(ABC):
    @abstractmethod
    def __init__(self, cliente, numConta, saldo) -> None:
        self.__cliente = cliente
        self.__numConta = numConta
        self.saldo = saldo
    @property
    def cliente(self):
        return self.__cliente
    @property
    def numConta(self):
        return self.__numConta
    def sacar(self,valor):
        if valor > self.saldo:
            print(f'{self.cliente} seu saldo é insuficiente!')
        else:
            self.saldo -= valor
    def depositar(self,valor):
        self.saldo += valor

class ContaPoupança(ContaBancaria):
    def __init__(self, cliente, numConta, saldo,rendimento) -> None:
        super().__init__(cliente, numConta, saldo)
        self.rendimento = rendimento
    def calcularNovoSaldo(self):
        self.saldo += self.saldo*(self.rendimento/100)

class ContaEspecial(ContaBancaria):
    def __init__(self, cliente, numConta, saldo, limite) -> None:
        super().__init__(cliente, numConta, saldo)
        self.limite = limite
    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print(f'{self.cliente} seu saldo é insuficiente!')
        else:
            self.saldo -= valor