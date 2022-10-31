class ContaBancaria:
    def __init__(self,cliente,num_conta,saldo):
        self.cliente = cliente
        self.num_conta = num_conta
        self.saldo = saldo
    def sacar(self,saque):
        if saque < self.saldo:
            self.saldo -= saque
            print (f'R$ {self.saldo}')
            return self.saldo
    '''def depositar(self,saldo):
        pass'''
class ContaPoupança(ContaBancaria):
    def __init__(self,cliente,num_conta,saldo,dia_de_rendimento):
        super().__init__(cliente,num_conta,saldo)
        self.dia_de_rendimento = dia_de_rendimento
    def novoSaldo(self,saldo):
        pass
class ContaEspecial(ContaBancaria):
    def __init__(self,cliente,num_conta,saldo,limite):
        super().__init__(cliente,num_conta,saldo)
        self.limite = limite
    def sacar(self,saque):
        if saque < self.limite:
            self.saldo -= self.limite 
            print (f'R$ {self.saldo}')
            return self.saldo
c1 = ContaEspecial('bryan',123,100,1000)
print(c1.sacar(30))