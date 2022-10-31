import sqlite3

conexao = sqlite3.connect('Sla/bancoTeste.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS pessoas('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT NOT NULL,'
'peso REAL'
')')
#INSERT INTO = CREATE CRUD, COMMIT
cursor.execute('INSERT INTO pessoas (nome, peso) VALUES (?, ?)', ("Alencar", 100))
conexao.commit()
#UPDATE, COMMIT
cursor.execute('UPDATE pessoas SET peso = ?, nome = ? WHERE id = 1',(120, "José"))
conexao.commit()
#DELETE, COMMIT
cursor.execute('DELETE FROM pessoas WHERE id = 2')
conexao.commit()
#READ
cursor.execute('SELECT * FROM pessoas')
for linha in cursor.fetchall():
    print(linha)

cursor.close
conexao.cursor