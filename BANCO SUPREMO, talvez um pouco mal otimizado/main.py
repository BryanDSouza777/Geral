from ast import Break
import random
import sqlite3

conexao = sqlite3.connect('BANCO SUPREMO, talvez um pouco mal otimizado/baseDeDados.db')
cursor = conexao.cursor()

acessar = int(input('Desejar...\n1-Acessar uma ja existente\n2-Criar uma conta\n\n: '))
def mostrarBancoDeDados():
    cursor.execute('SELECT * FROM contabancaria')
    for linha in cursor.fetchall():
        print(linha)
match acessar:
    case 2:
        print('### Criar Conta ###')
        
        email = input('\nDigite seu email: ')
        while True:
            senha = input('\nDigite seu senha\n: ')
            if len(senha) < 12:
                print ('\nSenha deve conter pelo menos 12 Caracteres.')
                continue
            else:
                break
        while True:
            nome = input('\nDigite seu nome: ')
            y = nome.isalpha()
            if y == True:
                break
            else:
                print('Nome não pode conter números.')
                continue
        while True:
            idade = int(input('\nDigite sua idade: '))
            if idade < 18:
                print('\nVocê é menor de idade.\nNão foi possivel criar uma conta bancaria.')
                exit()
            else: break
        chavepix = input('\nDigite sua Chave Pix\n: ')
        while True:
            TipoConta = int(input('\nQual conta deseja criar?\n1-Conta Especial\n2-Conta Poupança\n3-Sair\n\n: '))
            if TipoConta == 1:
                contadb = 'Conta Especial'
                break
            elif TipoConta == 2:
                contadb = 'Conta Poupança'
                break
            else:
                continue
        contadb = str(contadb)
        
        #aN = agencia, Numbers
        aN = []
        for agenciaNum in range(5):
            x = random.randint(0,9)
            aN.append(x)
        agencia = (f'{aN[0]}{aN[1]}{aN[2]}{aN[3]}-{aN[4]}')

        #nCn = numero de Conta, numbers
        nCn = []
        for ContaNum in range(6):
            y = random.randint(0,9)
            nCn.append(y)
        numConta = (f'{nCn[0]}{nCn[1]}{nCn[2]}{nCn[3]}{nCn[4]}-{nCn[5]}')
        limite = random.randint(500,5000)
        if TipoConta == 1 or TipoConta == 2:
                
            print('\nGerando conta...')
            print(f'\nAgencia: {agencia}\nNumero de Conta: {numConta}\nLimite: R$ {limite}')
        else:
            print('')

def insertTable():
    cursor.execute('INSERT INTO contabancaria(nome,idade,chavepix,contadb,saldo,numConta,agencia,limite,email,senha) VALUES (?,?,?,?,?,?,?,?,?,?)',(nome,idade,chavepix,contadb,0,numConta,agencia,limite,email,senha))
    conexao.commit()

cursor.execute('CREATE TABLE IF NOT EXISTS contabancaria('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT,'
'idade INTEGER,'
'chavepix TEXT NOT NULL,'
'contadb TEXT,'
'saldo REAL,'
'numConta TEXT,'
'agencia TEXT,'
'limite REAL,'
'email TEXT UNIQUE,'
'senha TEXT'
')')
if acessar == 2:
    insertTable()
    exit()

def entrarConta():
    senhaTemp = input('Digite sua senha\n: ')
    verifSenha = ("('"+(senhaTemp)+"',)")
    try:
        if verifSenha == senha_db:
            print('\nConta Bancaria acessada com sucesso.\n')
        elif verifSenha != senha_db:
            print('\nNão foi possivel acessar a Conta Bancaria.\n')
            exit()
    except:
        print('\nNão foi possivel acessar a Conta Bancaria.\n')
        exit()

if acessar == 1:
    verifEmail = input('Digite seu email\n: ')
cursor.execute(f'SELECT senha FROM contabancaria WHERE email = "{verifEmail}"')
for linha in cursor.fetchall():
    senha_db = linha
    senha_db = str(senha_db)

if acessar == 1:
    entrarConta()

cursor.execute(f'SELECT nome FROM contabancaria WHERE email = "{verifEmail}"')
for linha2 in cursor.fetchall():
    nome_db = linha2
    nome_db = str(nome_db)
letras = "()',"
nome_db = ''.join( x for x in nome_db if x not in letras)

cursor.execute(f'SELECT limite FROM contabancaria WHERE email = "{verifEmail}"')
for linha3 in cursor.fetchall():
    limite_db = linha3
    limite_db = str(limite_db)
limite_db = ''.join( x for x in limite_db if x not in letras)
limite_db = float(limite_db)
    
cursor.execute(f'SELECT saldo FROM contabancaria WHERE email = "{verifEmail}"')
for linha5 in cursor.fetchall():
    saldo_db = linha5
    saldo_db = str(saldo_db)
saldo_db = ''.join( x for x in saldo_db if x not in letras)
saldo_db = float(saldo_db)

cursor.execute(f'SELECT contadb FROM contabancaria WHERE email = "{verifEmail}"')
for linha7 in cursor.fetchall():
    conta_db = linha7
    conta_db = str(conta_db)
conta_db = ''.join( x for x in conta_db if x not in letras)

def usarContaEspecial(saldoCE):
    while True:
        print(f'R$ {saldoCE}\n')
        dinheiro = float(input('Quanto deseja depositar?: R$ '))
        saldoCE += dinheiro
        print(f'R$ {saldoCE}\n')
        dinheiro = float(input('Quanto deseja sacar?: R$ '))
        if dinheiro > saldoCE + limite_db:
            print(f'{nome_db}, seu saldo é insuficiente!')
        else:
            saldoCE -= dinheiro
        print(f'R$ {saldoCE}\n')
        cursor.execute(f'UPDATE contabancaria SET saldo = ? WHERE email = ?',(saldoCE, verifEmail))
        conexao.commit()
        dsj1 = int(input('Deseja fazer uma transferencia?\n1-Sim\n2-Não\n\n: '))
        match dsj1:
            case 1:
                idTransf = input('\nDigite o numero de conta do destinatário\n: ')
                valor = int(input('\nDigite o valor a ser transferido\n: R$ '))
                valormenos = saldoCE - valor
                cursor.execute(f'SELECT saldo FROM contabancaria WHERE numConta = "{idTransf}"')
                for linha in cursor.fetchall():
                    saldo_dt = linha
                    saldo_dt = str(saldo_dt)
                saldo_dt = ''.join( x for x in saldo_dt if x not in letras)
                saldo_dt = float(saldo_dt)
                valormais = saldo_dt + valor
                cursor.execute('UPDATE contabancaria SET saldo = ? WHERE numConta = ?',(valormais, idTransf))
                conexao.commit()
                print('\nTranferencia Concluida\n')
                cursor.execute('UPDATE contabancaria SET saldo = ? WHERE email = ?',(valormenos, verifEmail))
                conexao.commit()
            case 2:
                break
        dsj = int(input('Deseja continuar?\n1-Sim\n2-Não\n\n: '))
        match dsj:
            case 1: continue
            case 2: exit()
            case _: exit()

def usarContaPoupança(saldoCP,rendimento):
    while True:
        print(f'\nR$ {saldoCP}\n')
        dinheiro = float(input('Quanto deseja depositar?: R$ '))
        saldoCP += dinheiro
        print(f'R$ {saldoCP}\n')
        dinheiro = float(input('Quanto deseja sacar?: R$ '))
        if dinheiro > saldoCP + limite_db:
            print(f'{nome_db}, seu saldo é insuficiente!')
        else:
            saldoCP -= dinheiro
        print(f'R$ {saldoCP}\n')
        cursor.execute(f'UPDATE contabancaria SET saldo = ? WHERE email = ?',(saldoCP, verifEmail))
        conexao.commit()
        rendendo = saldoCP*(rendimento/100)
        saldoCP += rendendo
        print(f'Rendendo: {rendimento}% = R$ {rendendo}')
        print(f'R$ {saldoCP}\n')
        dsj1 = int(input('Deseja fazer uma transferencia?\n1-Sim\n2-Não\n\n: '))
        match dsj1:
            case 1:
                idTransf = input('\nDigite o numero de conta do destinatário\n: ')
                valor = int(input('\nDigite o valor a ser transferido\n: '))
                valormenos = saldoCP - valor
                cursor.execute(f'SELECT saldo FROM contabancaria WHERE numConta = "{idTransf}"')
                for linha in cursor.fetchall():
                    saldo_dt = linha
                    saldo_dt = str(saldo_dt)
                saldo_dt = ''.join( x for x in saldo_dt if x not in letras)
                saldo_dt = float(saldo_dt)
                valormais = saldo_dt + valor
                cursor.execute('UPDATE contabancaria SET saldo = ? WHERE numConta = ?',(valormais, idTransf))
                conexao.commit()
                print('\nTranferencia Concluida\n')
                cursor.execute('UPDATE contabancaria SET saldo = ? WHERE email = ?',(valormenos, verifEmail))
                conexao.commit()
            case 2:
                break
        dsj = int(input('Deseja continuar?\n1-Sim\n2-Não\n\n: '))
        match dsj:
            case 1: continue
            case 2: exit()
            case _: exit()

match conta_db:
    case 'Conta Especial':
        print('\n### Acessar a Conta do Banco ###\n### Conta Especial ###')
        usarContaEspecial(saldo_db)
    case 'Conta Poupança':
        print('\n### Acessar a Conta do Banco ###\n### Conta Poupança ###')
        usarContaPoupança(saldo_db,10)

cursor.close()
conexao.close()