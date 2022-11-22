import sqlite3
conexao = sqlite3.connect('contas.db')
cursor = conexao.cursor()

letras = "()',"
class Main():
    def verifEmail(self):
        try:
            email = input('\nDigite seu email\n: ')
            self.email = email
            cursor.execute(f'SELECT email FROM Conta WHERE email = "{self.email}"')
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
        cursor.execute(f'SELECT senha FROM Conta WHERE email = "{self.email}"')
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
    def menu(self):
        while True:
            MainMenu=input('1-Adicionar item à lista\n2-Remover Item da Lista\n3-Ver Lista\n4-Modificar Salario\n5-Visualizar Gastos e Resto\n6-Deletar Conta\n\n: ')
            match MainMenu:
                case '1':
                    produto=input('Nome do Produto\n: ')
                    while True:
                        try:
                            preço=float(input('Valor do Produto\n: '))
                        except:
                            print('Digite um valor Real, não utilize letras!')
                            continue
                        break
                    cursor.execute('INSERT INTO Gastos(Produto,Preço,Conta) VALUES(?,?,?)',(produto,preço,self.email))
                    conexao.commit()
                    print(f'{produto}(R$ {preço}) foi adicionado à lista!')
                    continue
                case '2':
                    cursor.execute(f'SELECT Produto FROM Gastos WHERE Conta = "{self.email}"')
                    for linha in cursor.fetchall():
                        produtos = linha
                        produtos = str(produtos)
                        produtos = ''.join( x for x in produtos if x not in letras)
                case '3':
                    prodtemp = []
                    x=0
                    preçtemp = []
                    y=0
                    cursor.execute(f'SELECT Produto FROM Gastos WHERE Conta = "{self.email}"')
                    for linha in cursor.fetchall():
                        produtos = linha
                        produtos = str(produtos)
                        produtos = ''.join( x for x in produtos if x not in letras)
                        x += 1
                        prodtemp.append(produtos)
                    cursor.execute(f'SELECT Preço FROM Gastos WHERE Conta = "{self.email}"')
                    for linha in cursor.fetchall():
                        preços = linha
                        preços = str(preços)
                        preços = ''.join( x for x in preços if x not in letras)
                        preçtemp.append(preços)
                    for i in str(len(prodtemp)):
                        print(prodtemp)
                        print(preçtemp)
                        print(f'{int(i)+1} - {prodtemp[int(i)]}({preçtemp[int(i)]})')
                    


a = Main()
while True:
    login = input('1-Entrar\n2-Criar conta\n\n: ')
    match login:
        case '1':
            a.acessarConta()
            a.menu()
            break
        case '2':
            nome=input('Digite seu Nome\n: ')
            while True:
                email=input('Digite seu Email\n: ')
                if '@' not in email and '.com' not in email:
                    print('Senha deve conter "@" e ".com"')
                    continue
                else: break
            while True:
                senha=input('Digite sua Senha\n: ')
                if len(senha) < 8:
                    print('Senha deve conter 8+ digitos.')
                    continue
                else: break
            cursor.execute('INSERT INTO Conta(Nome,email,senha) VALUES(?,?,?)',(nome,email,senha))
            conexao.commit()
            print('\nConta criada com Sucesso')
            while True:
                loginPósCad = (input(f'\nDeseja...\n1-Fazer Login\n2-Sair\n\n: '))
                if loginPósCad != '1' and loginPósCad != '2':
                    print('Digite apenas 1 ou 2!')
                    continue
                else: break
            match loginPósCad:
                case '1':
                    a.acessarConta()
                case '2':
                    exit()
            break
        case _:
            print('Digite apenas "1" ou "2"')
            continue

cursor.close()
conexao.close()