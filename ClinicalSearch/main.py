from datetime import date
import sqlite3

conexao = sqlite3.connect('ClinicalSearch/clinicalsearch.db')
cursor = conexao.cursor()
while True:
    login = input('Deseja...\n1-Fazer Login\n2-Cadastrar-se\n\n: ')
    if login != '1' and login != '2':
        print('Digite apenas 1 ou 2.')
        continue
    else: break
letras = "()',"
class VerifConta():
    def verifEmail(self):
        try:
            email = input('\nDigite seu email\n: ')
            self.email = email
            cursor.execute(f'SELECT email FROM conta WHERE email = "{self.email}"')
            for linha in cursor.fetchall():
                email_db = linha
                email_db = str(email_db)
                email_db = ''.join( x for x in email_db if x not in letras)
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
        if self.senha == senha_db:
            pass
        else:
            print('Senha Inválida')
            self.verifSenha()

def acessarConta(self):
        self.verifEmail()
        self.verifSenha()
        self.menu()

cliente = VerifConta()
match login:
    case '1':
        cliente.acessarConta()
    case '2':
        print(f'\n### Criar Conta ###')
        while True:
            nome = input('Digite seu nome completo\n: ')
            nomeReplace = nome.replace(' ','')
            if nomeReplace.isalpha() == True:
                break
            else: continue
        while True:
            aniversario = input(f'\nDigite seu aniversário\n(dd/mm/yyyy)\n\n: ')
            dmyTemp = aniversario.split('/')
            dmy = []
            for i in dmyTemp:
                dmy.append(int(i))
            dia = dmy[0]
            mes = dmy[1]
            ano = dmy[2]
            idade = int((date.today() - date(ano,mes,dia)).days / 365.25)
            print(f'Você tem {idade} anos!')
            if idade < 16:
                print('\nVocê deve ter no mínimo 16 anos')
                continue
            else: break
        while True:
            email = input('\nDigite seu email\n: ')
            if '@' in email and '.com'in email:
                break
            else:
                print('Email precisa de "@" e ".com"!')
                continue
        while True:
            senha = input('\nDigite seu senha\n: ')
            if len(senha) < 6:
                print ('Senha deve conter no mínimo 6 caracteres!')
                continue
            else: break
        cursor.execute('CREATE TABLE IF NOT EXISTS "conta"('
        'email TEXT PRIMARY KEY NOT NULL UNIQUE,'
        'senha TEXT NOT NULL'
        ')')
        if login == 2:
            cursor.execute('INSERT INTO Login(nome,aniversario,email,senha) VALUES (?,?,?,?)',(nome,aniversario,email,senha))
            conexao.commit()

while True:
    dsj = input('Deseja...\n1-Marcar consulta\n2-Ver sintomas\n\n: ')
    if dsj != '1' and dsj != '2':
        print('Digite apenas 1 ou 2.')
        continue
    else: break
match dsj:
    case '1':
        pass
    case '2':
        pass


cursor.close()
conexao.close()