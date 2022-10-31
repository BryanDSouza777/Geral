import sqlite3
conexao = sqlite3.connect("pessoa.db")
cursor = conexao.cursor()

nome = input('Nome: ')
peso = float(input('Peso: '))
idade = int(input('Idade: '))
sexo = input('Sexo: ')
classeSocial = input('Classe Social: ')

cursor.execute('CREATE TABLE IF NOT EXISTS cliente('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT,'
'peso REAL,'
'idade INTEGER,'
'sexo TEXT,'
'classeSocial TEXT'
')')

cursor.execute('INSERT INTO cliente(nome,peso,idade,sexo,classeSocial) VALUES (?,?,?,?,?)',(nome,peso,idade,sexo,classeSocial))
conexao.commit()
print(f'\n____________________60 Kg____________________')
cursor.execute('SELECT * FROM cliente WHERE peso > 60')
for linha in cursor.fetchall():
    print(linha)
print(f'\n___________________MULHERES___________________')
cursor.execute('SELECT * FROM cliente WHERE sexo == "F"')
for linha in cursor.fetchall():
    print(linha)
print(f'\n______________Classe Social Alta______________')
cursor.execute('SELECT * FROM cliente WHERE classeSocial == "Alta"')
for linha in cursor.fetchall():
    print(linha)
print(f'\n____________+60Kg, 18y, F, CS Alta+____________')
cursor.execute('SELECT * FROM cliente WHERE peso > 60 AND idade > 18 AND sexo == "F" AND classeSocial == "Alta"')
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()