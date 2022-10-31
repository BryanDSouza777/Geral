import random
class Funcionarios:
    def __init__ (self,nome,salario,data_admi):
        self.nomef = nome
        self.salariof = salario
        self.admisaof = data_admi
    
class Departamento:
    def __init__(self,nome):
        self.nomed = nome
        self.funcionarios = []
    def inserirFuncionario(self,nome,salario,dataadmisao):
        self.funcionarios.append(Funcionarios(nome,salario,dataadmisao))
    def lista(self):
        for funcionario in self.funcionarios:
            print (f'{funcionario.nomef}, R$ {funcionario.salariof:.2f}, {funcionario.admisaof}')
    def contratar(self, funcionario, salario, data):
        self.inserirFuncionario(funcionario,salario,data)
        '''print(f'{funcionario}, R${salario}, {data}')'''
    def aumento(self):
        for funcionario in self.funcionarios:
            funcionario.salariof*=1.10
        
class Empresa:
    def __init__(self,nome):
        self.nomee = nome
        self.departamentos = []
    def inserirDepartamento(self,nome):
        self.departamentos.append(Departamento(nome))

    def generate_cnpj(self):
        cnpj = [random.randrange(10) for a in range(8)] + [0, 0, 0, 1]
        for a in range(2):
            value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
            digit = 11 - value % 11
            cnpj.append(digit if digit < 10 else 0)

        return "".join(str(x) for x in cnpj)