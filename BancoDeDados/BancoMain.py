import linecache
import sqlite3
#Insert = Create
conexao = sqlite3.connect('Banco de Dados/baseDeDados.db')
cursor = conexao.cursor()

nome = input('Nome: ')
saldo = float(input('Saldo: '))
numConta = (input('Numero de Conta: '))
agencia = (input('Agência: '))

cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT,'
'saldo REAL,'
'numConta TEXT,'
'agencia TEXT'
')')
cursor.execute(f'INSERT INTO clientes(nome,saldo,numConta,agencia) VALUES ("{nome}",{saldo},"{numConta}","{agencia}")')
conexao.commit()
#cursor.execute(f'DELETE FROM clientes WHERE id=4')

#cursor.execute('SELECT saldo FROM clientes WHERE id == 3')
cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()