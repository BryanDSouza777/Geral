import sqlite3

conexao = sqlite3.connect('BancoDeDados/xy.db')
cursor = conexao.cursor()

acessar = int(input('Desejar...\n1-Acessar uma ja existente\n2-Criar uma conta\n\n: '))
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

    def criarPerfil1(self):
        self.perfil(self.email)

    def criarPerfil2(self):
        self.perfil(email)
    
    def listaDeFilmes(self,lista):
        dsj = int(input('Deseja adicionar ou remover algum filme de sua lista?\n1-Sim\n2-Não\n\n: '))
        if dsj == 1:
            while True:
                mudarLista = int(input('Deseja...\n1-Adicionar algum filme à lista\n2-Remover algum filme à lista?\n\n: '))
                if mudarLista == 1:
                    filme = input('Nome do filme\n\n:')
                    lista.append(filme)
                    repetir = int(input('Deseja adicionar outtro filme?\n1-Sim\n2-Não\n\n: '))
                    if repetir == 1: continue
                    else: break
        if dsj == 2:
            self.voltarMenu()
    
    def menu(self):
        dsj = int(input(f'\nDeseja...\n1-Criar um perfil\n2-Entrar em um perfil\n3-Ver todos os perfis\n4-Alterar nome de Perfil\n5-Conectar em outra conta\n6-Alterar a senha\n7-Excluir um perfil\n8-Excluir conta\n9-Sair\n\n: '))
        match dsj:
            case 1: self.criarPerfil1()
            case 2:
                self.perfil()
                cursor.execute(f'SELECT * FROM perfis WHERE email_Conta = "{self.email}"')
                for linha in cursor.fetchall():
                    print(linha)
                id = int(input('\nQual o perfil(id) que você deseja mudar o nome?\n:'))

                cursor.execute(f'SELECT Nome FROM perfis WHERE id = {id}')
                for linha in cursor.fetchall():
                    nomeDoPerfil = linha
                print(f'Olá, {nomeDoPerfil}')
                filmesFav = []
                self.listaDeFilmes(filmesFav)
                
                
            case 3: self.mostrarPerfis()
            case 4: self.mudarNome()
            case 5: self.acessarConta()
            case 6: self.mudarSenha()
            case 7:
                certeza = int(input('Tem certeza que deseja excluir seu perfil?\n1-Sim\n2-Não\n\n: '))
                if certeza == 1:
                    cursor.execute(f'SELECT * FROM perfis WHERE email_Conta = "{self.email}"')
                    for linha in cursor.fetchall():
                        print(linha)
                    id = int(input('\nQual o perfil(id) que você deseja mudar o nome?\n:'))
                    cursor.execute(f'DELETE FROM perfis WHERE id = {id}')
                    conexao.commit()
                    self.voltarMenu()
                else:
                    self.voltarMenu()
            case 8:
                cursor.execute(f'DELETE FROM perfis WHERE email_Conta = "{self.email}"')
                conexao.commit()
                cursor.execute(f'DELETE FROM conta WHERE email = "{self.email}"')
                conexao.commit()
                print(f'\nConta deletada com Sucesso!')
                dsj = int(input('Deseja conectar em outra conta?\n1-Sim\n2-Não\n\n: '))
                if dsj == 1:
                    self.acessarConta()
                else: exit()
            case 9:
                exit()
            case _:
                exit()

    def voltarMenu(self):
        dsj = int(input('\nDeseja ir ao menu?\n1-Sim\n2-Não\n\n: '))
        if dsj == 1:
            self.menu()
        else: exit()

    def perfil(self,emailDef):
        criar = int(input('Desejar...\n1-Criar um perfil\n2-Acessar um perfil\n\n: '))
        match criar:
            case 1:
                email_Conta = emailDef
                nome = input('\nDigite o nome do seu perfil: ')
                imagem = int(input('\nDigite...\n1-Perfil com imagem\n2-Perfil sem imagem\n\n: '))
                if imagem == 1:
                    imagem = bool(True)
                elif imagem == 2:
                    imagem = bool(False)
                else:
                    imagem = bool(False)
                cursor.execute('CREATE TABLE IF NOT EXISTS "perfis"('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'Nome TEXT NOT NULL,'
                'imagem BLOB,'
                'email_Conta TEXT,'
                'FOREIGN KEY("email_Conta") REFERENCES "conta"("email")'
                ')')
                cursor.execute('INSERT INTO perfis(Nome,imagem,email_Conta) VALUES (?,?,?)',(nome,imagem,email_Conta))
                conexao.commit()
                self.voltarMenu()
            case 2:
                pass
        
    def acessarConta(self):
        self.verifEmail()
        self.verifSenha()
        self.menu()

    def mostrarPerfis(self):
        print('')
        cursor.execute(f'SELECT * FROM perfis WHERE email_Conta = "{self.email}"')
        for linha in cursor.fetchall():
            print(linha)
        self.voltarMenu()


    def mudarNome(self):
        cursor.execute(f'SELECT * FROM perfis WHERE email_Conta = "{self.email}"')
        for linha in cursor.fetchall():
            print(linha)
        id = int(input('\nQual o perfil(id) que você deseja mudar o nome?\n:'))
        nome = input(f'\nNome: ')
        cursor.execute(f'UPDATE perfis SET Nome = ? WHERE id = {id}',(nome,))
        conexao.commit()
        print(f'\nNome alterado com sucesso!')
        self.menu()

    def mudarSenha(self):
        certeza = int(input('Tem certeza que deseja alterar sua senha?\n1-Sim\n2-Não\n\n: '))
        if certeza == 1:
            novasenha = input('Digite sua nova senha\n\n: ')
            cursor.execute(f'UPDATE conta SET senha = "{novasenha}" WHERE email = "{self.email}"')
            conexao.commit()
            self.voltarMenu()
        else:
            self.voltarMenu()

cliente = VerifConta()
match acessar:
    case 1:
        cliente.acessarConta()
    case 2:
        print('### Criar Conta ###')
        email = input('\nDigite seu email\n: ')
        senha = input('\nDigite seu senha\n: ')
        cursor.execute('CREATE TABLE IF NOT EXISTS "conta"('
        'email TEXT PRIMARY KEY NOT NULL UNIQUE,'
        'senha TEXT NOT NULL'
        ')')
        if acessar == 2:
            cursor.execute('INSERT INTO conta(email,senha) VALUES (?,?)',(email,senha))
            conexao.commit()
        criar = int(input(f'\nDesejar criar um perfil?\n1-Sim\n2-Não\n\n: '))
        if criar == 1:
            cliente.criarPerfil2()
        else: exit()


cursor.close()
conexao.close()