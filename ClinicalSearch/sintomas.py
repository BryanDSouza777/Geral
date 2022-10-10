def sintomaspy(email):
    import sqlite3

    conexao = sqlite3.connect('ClinicalSearch/clinicalsearch.db')
    cursor = conexao.cursor()
    letras = "()',"
    meus_sintomas = []
    corpo = []
    def diaDaSemana():
        while True:
            diaSemana = input('Deseja marcar uma consulta para que dia da semana:\n1 - Domingo\n2 - Segunda-Feira\n3 - Terça-Feira\n4 - Quarta-Feira\n5 - Quinta-Feira\n6 - Sexta-Feira\n7 - Sábado\n\n: ')
            if diaSemana != '1' and diaSemana != '2' and diaSemana != '3' and diaSemana != '4' and diaSemana != '5' and diaSemana != '6' and diaSemana != '7':
                print('Digite apenas um numero de 1 à 7!')
                continue
            else: break
        match diaSemana:
            case '1': diaSemana = 'Domingo'
            case '2': diaSemana = 'Segunda-Feira'
            case '3': diaSemana = 'Terça-Feira'
            case '4': diaSemana = 'Quarta-Feira'
            case '5': diaSemana = 'Quinta-Feira'
            case '6': diaSemana = 'Sexta-Feira'
            case '7': diaSemana = 'Sábado'
        return diaSemana
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
            print('Você tem que ir a um Cardiologista\n')
            while True:
                data = diaDaSemana()
                print('')
                cursor.execute(f'SELECT id, nomeMedico FROM NomeMedico WHERE "{data}" = "y" AND Especialidade = "Cardiologista"')
                for linha in cursor.fetchall():
                    nomeMedico = linha
                    print(nomeMedico)
                dsj = input(f'\nDeseja alterar a data?\n1 - Sim\n2 - Não\n\n: ')
                if dsj == '1': continue
                elif dsj == '2': break
                else:
                    print('Digite apenas 1 ou 2!')
                    continue
                #continuar com horario
            
            cursor.execute('INSERT INTO HoraMarcada(Profissional,Data,Horario,email_Paciente) VALUES (?,?,?,?)', ('Cardiologista',data,horario(),email))
            conexao.commit()
            print('Consulta marcada com um Cardiologista!')
        elif maior == corpPulmão:
            cursor.execute('INSERT INTO HoraMarcada(Profissional,Data,Horario,email_Paciente) VALUES (?,?,?,?)', ('Pneumologista',data(),horario(),email))
            conexao.commit()
            print('Consulta marcada com um Pneumologista!')
        elif maior == corpEstomago:
            cursor.execute('INSERT INTO HoraMarcada(Profissional,Data,Horario,email_Paciente) VALUES (?,?,?,?)', ('gastroenterologista',data(),horario(),email))
            conexao.commit()
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
                dsjDeletar = input(f'\nDeseja deletar algum sintoma de sua lista?\n1-Sim\n2-Não\n\n: ')
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
        def marcarConsulta(medico):
            cursor.execute('INSERT INTO HoraMarcada(Profissional,Data,Horario,email_Paciente) VALUES (?,?,?,?)', (medico,data(),horario(),email))
            conexao.commit()
            print('Consulta marcada com um Pneumologista!')
    menu()
    cursor.close()
    conexao.close()