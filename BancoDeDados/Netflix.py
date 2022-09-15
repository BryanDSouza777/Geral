import email
import sqlite3

conexao = sqlite3.connect('xy.db')
cursor = conexao.cursor()

acessar = int(input('Desejar...\n1-Acessar uma ja existente\n2-Criar uma conta\n\n: '))
letras = "()',"
class VerifConta():
    def __init__(self) -> None:
        pass
    def verifEmail(self):
        try:
            email = input('\nDigite seu email\n: ')
            self.email = email
            cursor.execute(f'SELECT email FROM conta WHERE email = "{self.email}"')
            for linha in cursor.fetchall():
                email_db = linha
                email_db = str(email_db)
                email_db = ''.join( x for x in email_db if x not in letras)
                print(f'{email_db}\n{self.email}')
            if email_db == self.email:
                pass
        except:
            print('Email Inválido.')
            self.verifEmail()
    def verifSenha(self):
        self.senha = input('\nDigite sua senha\n: ')
        cursor.execute(f'SELECT senha FROM conta WHERE email = "{self.email}"')
        for linha in cursor.fetchall():
            senha_db = linha
            senha_db = str(senha_db)
            senha_db = ''.join( x for x in senha_db if x not in letras)
            print(f'{senha_db}\n{senha}')
        if self.senha == senha_db:
            pass
        else: self.verifSenha()
                    
match acessar:
    case 1:
        cliente = VerifConta()
        cliente.verifEmail()
        cliente.verifSenha()
        criar = int(input(f'\nDesejar...\n1-Criar um perfil\n2-Acessar um perfil\n\n: '))
    case 2:
        print('### Criar Conta ###')
        email = input('\nDigite seu email: ')
        senha = input('\nDigite seu senha: ')

def insertTable():
    cursor.execute('INSERT INTO conta(email,senha) VALUES (?,?)',(email,senha))
    conexao.commit()

cursor.execute('CREATE TABLE IF NOT EXISTS "conta"('
'email TEXT PRIMARY KEY NOT NULL UNIQUE,'
'senha TEXT NOT NULL'
')')

cursor.execute('CREATE TABLE IF NOT EXISTS "perfis"('
'Nome TEXT NOT NULL,'
'imagem BLOB,'
'email_Conta TEXT,'
'FOREIGN KEY("email_Conta") REFERENCES "conta"("email")'
')')

if acessar == 2:
    insertTable()
    criar = int(input('Desejar...\n1-Criar um perfil\n2-Acessar um perfil\n\n: '))

match criar:
            case 1:
                print('### Criar Perfil ###')
                nome = input('\nDigite o nome do seu perfil: ')
                imagem = bool(input('\nDigite...\n1-Perfil com imagem\n2-Perfil sem imagem\n\n: '))
                if imagem == 1:
                    imagem = True
                elif imagem == 2:
                    imagem = False
                else:
                    imagem = False
                cursor.execute('INSERT INTO perfil(email,senha) VALUES (?,?)',(email,senha))
        
        







cursor.close()
conexao.close()