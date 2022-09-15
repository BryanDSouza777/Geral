import sqlite3
conexao = sqlite3.connect('Agenda/agenda.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS contatos('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT,'
'endereço TEXT,'
'numero INTEGER'
')')

class Contatos():
    def __init__(self) -> None:
        pass
    def inserirContatos(self,nome,endereço,numero):
        cursor.execute('INSERT INTO contatos(nome,endereço,numero) VALUES (?,?,?)',(nome,endereço,numero))
        conexao.commit()
    def alterarContatos(self):
        cursor.execute('UPDATE contatos SET nome = ? WHERE id = 1',("robson"))
        conexao.commit()
    def deletarContatos(self):
        cursor.execute('DELETE FROM contatos WHERE numero = 123')
        conexao.commit()
    def vizualizarContatos(self):
        cursor.execute('SELECT * FROM contatos')
        for i in cursor.fetchall():
            print(i)

contato = Contatos()
contato.alterarContatos()
contato.vizualizarContatos()


cursor.close()
conexao.close()