from Validador_CPF import CPF
import sqlite3

conexao = sqlite3.connect('Exercicio de Banco de Dados/BancoAgenda.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT NOT NULL,'
'telefone INTEGER NOT NULL UNIQUE,'
'endereço TEXT,'
'CPF REAL UNIQUE'
')')

cpfclass = CPF()

class Agenda:
    def mostrarTabela(self):
        item = int(input("Deseja ver oque da tabela:\n1-Nomes\n2-Telefones\n3-Endereços\n4-CPF's\n5-Todos\n\nResposta: "))
        match item:
            case 1: item = 'id, nome'
            case 2: item = 'id, telefone'
            case 3: item = 'id, endereço'
            case 4: item = 'id, CPF'
            case 5: item = '*'
        cursor.execute(f'SELECT {item} FROM clientes')
        for linha in cursor.fetchall():
            print(linha)
    def mostrarTabelaAuto(self,item):
        self.item = item
        match self.item:
            case 1: self.item = 'id, nome'
            case 2: self.item = 'id, telefone'
            case 3: self.item = 'id, endereço'
            case 4: self.item = 'id, CPF'
            case 5: self.item = '*'
        print('')
        cursor.execute(f'SELECT {self.item} FROM clientes')
        for linha in cursor.fetchall():
            print(linha)
    def inserirPessoas(self):
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        endereço = input('Endereço: ')
        cpf = input('CPF: ')
        cpfclass.escreverCPF(cpf)
        cursor.execute(f'INSERT INTO clientes(nome,telefone,endereço,cpf) VALUES (?,?,?,?)',(nome,telefone,endereço,cpf))
        conexao.commit()
        self.mostrarTabelaAuto(5)
    def alterarPessoas(self):
        dsj = int(input('Deseja alterar o:\n1-Nome\n2-Telefone\n3-Endereço\n4-CPF\n5-Todos\n\nResposta: '))
        id = int(input('\nQual o ID da pessoa que você deseja alterar algo?\n\nResposta: '))
        match dsj:
            case 1:
                nome = input('Nome: ')
                cursor.execute('UPDATE clientes SET nome = ? WHERE id = ?',(nome,id))
                conexao.commit()
                self.mostrarTabelaAuto(5)
            case 2:
                telefone = input('Telefone: ')
                cursor.execute('UPDATE clientes SET telefone = ? WHERE id = ?',(telefone,id))
                conexao.commit()
                self.mostrarTabelaAuto(5)
            case 3:
                endereço = input('Endereço: ')
                cursor.execute('UPDATE clientes SET endereço = ? WHERE id = ?',(endereço,id))
                conexao.commit()
                self.mostrarTabelaAuto(5)
            case 4:
                cpf = input('CPF: ')
                cursor.execute('UPDATE clientes SET cpf = ? WHERE id = ?',(cpf,id))
                conexao.commit()
                self.mostrarTabelaAuto(5)
            case 5:
                nome = input('Nome: ')
                telefone = input('Telefone: ')
                endereço = input('Endereço: ')
                cpf = input('CPF: ')
                cursor.execute('UPDATE clientes SET nome = ?, telefone = ?, endereço = ?, cpf = ? WHERE id = ?',(nome,telefone,endereço,cpf,id))
                conexao.commit()
                self.mostrarTabelaAuto(5)
    def deletarPessoas(self):
        id = int(input('Qual o ID da pessoa que você deseja deletar?\n\nResposta: '))
        cursor.execute('DELETE FROM clientes WHERE id = ?',(id,))
        conexao.commit()
        self.mostrarTabelaAuto(5)
    def listaTelefonica(self):
        self.mostrarTabelaAuto(2)
agenda = Agenda()
agenda.inserirPessoas()