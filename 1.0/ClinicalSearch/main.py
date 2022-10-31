from datetime import date
from sintomas import sintomaspy
from addHoraDisp import inserirHorarioMed
import sqlite3

conexao = sqlite3.connect('clinicalsearch.db')
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
            cursor.execute(f'SELECT email FROM Login WHERE email = "{self.email}"')
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
        cursor.execute(f'SELECT senha FROM Login WHERE email = "{self.email}"')
        for linha in cursor.fetchall():
            senha_db = linha
            senha_db = str(senha_db)
            senha_db = ''.join( x for x in senha_db if x not in letras)
        if self.senha == senha_db:
            pass
        else:
            print('Senha Inválida')
            self.verifSenha()

def acessarConta():
        cliente.verifEmail()
        cliente.verifSenha()

cliente = VerifConta()
match login:
    case '1':
        acessarConta()
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
        cursor.execute('INSERT INTO Login(nome,aniversario,idade,email,senha) VALUES (?,?,?,?,?)',(nome,aniversario,idade,email,senha))
        conexao.commit()
        print(f'\nConta Criada com Sucesso!')
        while True:
            loginPósCad = (input(f'\nDeseja...\n1-Fazer Login\n2-Sair\n\n: '))
            if loginPósCad != '1' and loginPósCad != '2':
                print('Digite apenas 1 ou 2!')
                continue
            else: break
        match loginPósCad:
            case '1':
                acessarConta()
            case '2':
                exit()
while True:
    dsj = input(f'\nDeseja...\n1-Ir para o Menu Principal\n2-Sair\n\n: ')
    if dsj != '1' and dsj != '2':
        print('Digite apenas 1 ou 2.')
        continue
    else: break
match dsj:
    case '1':
        sintomaspy(cliente.email)
    case '2':
        exit()
cursor.close()
conexao.close()