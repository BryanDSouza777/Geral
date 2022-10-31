from abc import ABC, abstractmethod
class Pessoa:
    def __init__(self,nome,idade):
        self.__nome = nome
        self.__idade = idade
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade

class Cliente(Pessoa):
    def __init__(self,nome,idade,conta):
        super().__init__(nome,idade)
        self.conta = conta
        
class Conta(ABC):
    def __init__(self, agencia, numConta, saldo):
        self.agencia = agencia
        self.numConta = numConta
        self.saldo = saldo
    @abstractmethod
    def sacar(self,valor):
        pass
    def depositar(self,valor):
        self.saldo += valor

class ContaPoupança(Conta):
    def __init__(self, nome, agencia, numConta, saldo, rendimento):
        self.nome = nome
        super().__init__(agencia, numConta, saldo)
        self.rendimento = rendimento
    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
            return self.saldo
        else:
            print(f'{self.nome}, seu saldo é insuficiente!')
    def calcularNovoSaldo(self):
        self.saldo += self.saldo*(self.rendimento/100)

class ContaEspecial(Conta):
    def __init__(self, nome, agencia, numConta, saldo, limite):
        self.nome = nome
        super().__init__(agencia, numConta, saldo)
        self.limite = limite
    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print(f'{self.nome}, seu saldo é insuficiente!')
        else:
            self.saldo -= valor