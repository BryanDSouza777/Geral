def sintomaspy(email):
    import sqlite3
    from random import randint
    from datetime import date

    def data():
        mes = (date.today()).month
        dia = (date.today()).day
        dia += randint (7,30)
        if dia > 30:
            dia = randint(1,30)
            if dia < (date.today()).day:
                mes += 1
        ano = (date.today()).year
        mes += randint(1,12)
        if mes > 12:
            mes = randint(1,12)
            if mes < (date.today()).month:
                ano += 1
        data = f'{dia}/{mes}/{ano}'
        return data

    def horario():
        hora = randint(8,23)
        minutos = randint(0,59)
        horário = f'{hora}:{minutos}'
        return horário

    conexao = sqlite3.connect('ClinicalSearch/clinicalsearch.db')
    cursor = conexao.cursor()
    letras = "()',"
    meus_sintomas = []
    corpo = []
    
    def MarcarHorario():
        corpCoração = corpo.count('coração')
        corpPulmão = corpo.count('pulmão')
        corpEstomago = corpo.count('estomago')
        if corpCoração > corpPulmão:
            maior = corpCoração
        else:
            maior = corpPulmão
        
        if maior > corpEstomago:
            pass
        else:
            maior = corpEstomago

        if maior == corpCoração:
            cursor.execute('INSERT INTO HoraMarcada(Profissional,Data,Horario,email_Paciente) VALUES (?,?,?,?)', ('Cardiologista',data(),horario(),email))
            print('Consulta marcada com um Cardiologista!')
        elif maior == corpPulmão:
            cursor.execute('INSERT INTO HoraMarcada(Profissional,Data,Horario,email_Paciente) VALUES (?,?,?,?)', ('Pneumologista',data(),horario(),email))
            print('Consulta marcada com um Pneumologista!')
        elif maior == corpEstomago:
            cursor.execute('INSERT INTO HoraMarcada(Profissional,Data,Horario,email_Paciente) VALUES (?,?,?,?)', ('gastroenterologista',data(),horario(),email))
            print('Consulta marcada com um Gastroenterologista!')
    class Sintomas:
        def __init__(self):
            pass
        def visualizarSintomas(self):
            cursor.execute('SELECT * FROM Sintomas ')
            print(f'\nID               SINTOMA\n')
            for linha in cursor.fetchall():        
                print(f'{linha[0]}        {linha[1]}')
            while True:
                dsj = input('\nDeseja...\n1-Ir para o Menu\n2-Sair\n\n: ')
                if dsj != '1' and dsj != '2':
                    print('Digite apenas 1 ou 2!')
                    continue
                else: break
            match dsj:
                case '1':
                    menu()
                case '2':
                    exit()
        def inserirSintoma(self):
            id = int(input(f'\nDigite o ID do sintoma desejado\n0 = Voltar ao menu\n\n: '))
            if id == 0:
                menu()
            if id > 45:
                self.inserirSintoma()
            cursor.execute(f'SELECT sintomas FROM Sintomas WHERE id = "{id}"')
            for linha in cursor.fetchall():
                sintoma = linha
                sintoma = ''.join( x for x in sintoma if x not in letras)
                print(f'\nSintoma "{sintoma}" adicionado à lista!')
                meus_sintomas.append(sintoma)
                cursor.execute(f'SELECT parte_corpo FROM Sintomas WHERE id = "{id}"')
                for  linha in cursor.fetchall():
                    parte_corpo = linha
                    parte_corpo = ''.join( x for x in parte_corpo if x not in letras)
                    corpo.append(parte_corpo)
            self.inserirSintoma()
        def visualizarMeusSintomas(self):
            print (f'Meus Sintomas:\n')           
            for i in range(len(meus_sintomas)):
                print(f'{i+1} - {meus_sintomas[i]}')

    a = Sintomas()
    def menu():
        while True:
            dsj = input('\nDeseja...\n1-Ver os Sintomas\n2-Selecionar Sintomas\n3-Ver seus Sintomas\n4-Marcar Consulta\n5-Sair\n\n: ')
            if dsj != '1' and dsj != '2' and dsj != '3' and dsj != '4' and dsj != '5':
                print('Digite apenas 1, 2, 3 ou 4!')
                continue
            else: break
        match dsj:
            case '1':
                a.visualizarSintomas()
            case '2':
                a.inserirSintoma()
            case '3':
                a.visualizarMeusSintomas()
                print(corpo)
                dsjDeletar = input('Deseja deletar algum sintoma de sua lista?\n1-Sim\n2-Não\n\n: ')
                match dsjDeletar:
                    case '1':
                        while True:
                            deletar = int(input('ID: '))
                            while True:
                                if deletar > len(meus_sintomas):
                                    continue
                                else: break
                            del(meus_sintomas[deletar-1])
                            a.visualizarMeusSintomas()
                            while True:
                                continuar = input('Deletar outro?\n1-Sim\n2-Não\n\n: ')
                                if continuar != '1' and continuar != '2':
                                    continue
                                else: break
                            match continuar:
                                case '1':
                                    continue
                                case '2':
                                    menu()
                    case '2':
                        menu()
            case '4':
                MarcarHorario()
            case '5':
                exit()
    menu()

    cursor.close()
    conexao.close()