import sqlite3
conexao = sqlite3.connect("banquito.db")
cursor = conexao.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS cliente('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT,'
'peso REAL'
')')
cursor.execute('INSERT INTO cliente(nome,peso) VALUES (?,?)',("Bruno",100))
conexao.commit()
cursor = conexao.execute('SELECT * FROM cliente WHERE peso < 80')
for linha in cursor.fetchall:
    print(linha)
cursor = conexao.execute('UPDATE cliente SET peso = ? WHERE id = 23',(58,))
conexao.commit()
cursor = conexao.execute('SELECT * FROM cliente WHERE peso <80')
for linha in cursor.fetchall:
    print(linha)
cursor.close()
conexao.close()