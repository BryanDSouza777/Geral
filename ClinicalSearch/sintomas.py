def sintomaspy(email):
    import sqlite3
    conexao = sqlite3.connect('clinicalsearch.db')
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
    def MarcarConsultaFinal(Especialidade):
        while True:
            data = diaDaSemana()
            idMedico = []
            print('')
            cursor.execute(f'SELECT id FROM NomeMedico WHERE "{data}" = "y" AND Especialidade = "{Especialidade}"')
            for linha in cursor.fetchall():
                idMedic = linha
                idMedic = str(idMedic)
                idMedic = ''.join( x for x in idMedic if x not in letras)
                idMedic = int(idMedic)
                idMedico.append(idMedic)
            cursor.execute(f'SELECT id, nomeMedico FROM NomeMedico WHERE "{data}" = "y" AND Especialidade = "{Especialidade}"')
            for linha in cursor.fetchall():
                nomesMedicos = linha
                print(nomesMedicos)
            dsj = input(f'\nDeseja alterar a data?\n1 - Sim\n2 - Não\n\n: ')
            if dsj == '1': continue
            elif dsj == '2': break
            else:
                print('Digite apenas 1 ou 2!')
                continue
        while True:
            try:
                selectMedico = int(input('Selecione um médico pelo id.\n: '))
            except:
                print('Digite um ID válido')
                continue
            if selectMedico not in idMedico:
                print('Digite um ID válido')
                continue
            else:
                break
        cursor.execute(f'SELECT nomeMedico FROM NomeMedico WHERE id = "{selectMedico}"')
        for linha in cursor.fetchall():
            nomeMedico = linha
            nomeMedico = ''.join( x for x in nomeMedico if x not in letras)
            print(f'\n{nomeMedico} selecionado!')
            print('\nDatas disponiveis:')
        idHrDisponivel = []
        cursor.execute(f'SELECT id FROM horariosDisponiveis WHERE diaSemana = "{data}" AND nomeMedico = "{nomeMedico}"')
        for linha in cursor.fetchall():
            idHrDisp = linha
            idHrDisp = str(idHrDisp)
            idHrDisp = ''.join( x for x in idHrDisp if x not in letras)
            idHrDisp = int(idHrDisp)
            idHrDisponivel.append(idHrDisp)
        cursor.execute(f'SELECT id, HorarioDisponivel FROM horariosDisponiveis WHERE diaSemana = "{data}" AND nomeMedico = "{nomeMedico}" AND Status = "Disponível"')
        for linha in cursor.fetchall():
            horariosDisponiveis = linha
            print(horariosDisponiveis)
        while True:
            try:
                selectHorario = int(input('Selecione um horário pelo id\n: '))
            except:
                print('Digite um ID válido')
                continue
            if selectHorario not in idHrDisponivel:
                print('Digite um ID válido')
                continue
            else:
                break
        cursor.execute(f'SELECT HorarioDisponivel FROM horariosDisponiveis WHERE diaSemana = "{data}" AND nomeMedico = "{nomeMedico}" AND id = "{selectHorario}"')
        for linha in cursor.fetchone():
            horariosMarcado = linha
        cursor.execute('INSERT INTO HoraMarcada(NomeMedic,Profissional,Data,Horario,email_Paciente) VALUES (?,?,?,?,?)', (nomeMedico,Especialidade,data,horariosMarcado,email))
        conexao.commit()
        cursor.execute(f'UPDATE horariosDisponiveis SET Status = "Indisponível" WHERE diaSemana = "{data}" AND nomeMedico = "{nomeMedico}" AND id = "{selectHorario}"')
        conexao.commit()
        cursor.execute(f'UPDATE horariosDisponiveis SET cliente = "{email}" WHERE diaSemana = "{data}" AND nomeMedico = "{nomeMedico}" AND id = "{selectHorario}"')
        conexao.commit()
        print(f'Consulta marcada com um {Especialidade}!')
        menu()

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
            print('Você precisa ir a um Cardiologista\n')
            MarcarConsultaFinal('Cardiologista')
        elif maior == corpPulmão:
            print('Você precisa ir a um Pneumologista\n')
            MarcarConsultaFinal('Pneumologista')
        elif maior == corpEstomago:
            print('Você precisa ir a um Gastroenterologista\n')
            MarcarConsultaFinal('gastroenterologista')
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
            id = int(input(f'\nDigite o ID do sintoma desejado\n0 = Para ao menu\n\n: '))
            if id == 0:
                a.menuSintomas()
            if id > 45:
                self.inserirSintoma()
            if id > 0 and id < 46:
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
        def menuSintomas(self):
            self.visualizarMeusSintomas()
            while True:
                dsj = input('\nDeseja...\n1-Visualizar seus Sintomas\n2-Deletar sintoma da lista\n3-Marcar Consulta com base nos sintomas\n4-Voltar ao menu\n\n: ')
                if dsj != '1' and dsj != '2' and dsj != '3' and dsj != '4':
                    print('Digite um numero de 1 à 4!')
                    continue
                else: break
            match dsj:
                case '1':
                    a.menuSintomas()
                case '2':
                    while True:
                        deletar = int(input('ID: '))
                        if deletar == 0:
                            break
                        if deletar > len(meus_sintomas):
                            continue
                        del(meus_sintomas[deletar-1])
                        a.visualizarMeusSintomas()
                    a.menuSintomas()
                case '3':
                    MarcarHorario()
                case '4':
                    menu()
        def visualizarMeusSintomas(self):
            print (f'Meus Sintomas:\n')           
            for i in range(len(meus_sintomas)):
                print(f'{i+1} - {meus_sintomas[i]}')
    idCons = []
    def consultasMarcadas():
        print('Consultas Marcadas:\n')
        cursor.execute(f'SELECT id, NomeMedic, Profissional, Data, Horario FROM HoraMarcada WHERE email_Paciente = "{email}"')
        for linha in cursor.fetchall():
            horaMarcada = linha
            print(horaMarcada)
        cursor.execute(f'SELECT id FROM HoraMarcada WHERE email_Paciente = "{email}"')
        for linha in cursor.fetchall():
            idConsultaTemp = linha
            idConsultaTemp = str(idConsultaTemp)
            idConsultaTemp = ''.join( x for x in idConsultaTemp if x not in letras)
            idCons.append(idConsultaTemp)
    a = Sintomas()
    def menu():
        while True:
            dsj = input('\nDeseja...\n1-Ver os Sintomas\n2-Selecionar Sintomas\n3-Menu dos Sintomas\n4-Marcar Consulta sem Sintomas\n5-Ver consultas marcadas\n6-Desmarcar Consulta\n7-Deletar Conta\n8-Sair\n\n: ')
            if dsj != '1' and dsj != '2' and dsj != '3' and dsj != '4' and dsj != '5' and dsj != '6' and dsj != '7' and dsj != '8':
                print('Digite apenas 1, 2, 3 ou 4!')
                continue
            else: break
        match dsj:
            case '1':
                a.visualizarSintomas()
            case '2':
                idtemp = []
                while True:
                    id = int(input(f'\nDigite o ID do sintoma desejado\n0 = Para ao menu\n\n: '))
                    if id in idtemp:
                        print(f"\nNão é possivel escolher ID's repetidos!")
                        continue
                    else: idtemp.append(id)
                    if id == 0:
                        break
                    if id > 45:
                        continue
                    if id > 0 and id < 46:
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
                a.menuSintomas()
            case '3':
                a.menuSintomas()
            case '4':
                while True:
                    dsjMedico = input('Deseja marcar uma consulta com:\n1 - Cardiologista\n2 - Pneumologista\n3 - Gastroenterologista\n\n: ')
                    if dsjMedico != '1' and dsjMedico != '2' and dsjMedico != '3':
                        print('Digite um numero de 1 à 3!')
                        continue
                    else: break
                match dsjMedico:
                    case '1': dsjMedico = 'Cardiologista'
                    case '2': dsjMedico = 'Pneumologista'
                    case '3': dsjMedico = 'gastroenterologista'
                MarcarConsultaFinal(dsjMedico)
            case '5':
                consultasMarcadas()
                menu()
            case '6':
                consultasMarcadas()
                while True:
                    idConsulta = input('Digite o ID da consulta que deseja deletar\n: ')
                    if idConsulta not in idCons:
                        print('Digite um ID válido')
                        continue
                    else: break
                cursor.execute(f'SELECT nomeMedic FROM HoraMarcada WHERE id = "{idConsulta}"')
                for linha in cursor.fetchall():
                    nomeMedic = linha
                    nomeMedic = ''.join( x for x in nomeMedic if x not in letras)
                cursor.execute(f'SELECT Data FROM HoraMarcada WHERE id = "{idConsulta}"')
                for linha in cursor.fetchall():
                    diaSem = linha
                    diaSem = ''.join( x for x in diaSem if x not in letras)
                cursor.execute(f'SELECT Horario FROM HoraMarcada WHERE id = "{idConsulta}"')
                for linha in cursor.fetchall():
                    horarDisp = linha
                    horarDisp = ''.join( x for x in horarDisp if x not in letras)
                cursor.execute(f'UPDATE horariosDisponiveis SET Status = "Disponível" WHERE nomeMedico = "{nomeMedic}" AND diaSemana = "{diaSem}" AND HorarioDisponivel = "{horarDisp}"')
                conexao.commit()
                cursor.execute(f'DELETE FROM HoraMarcada WHERE id = "{idConsulta}"')
                conexao.commit()
                menu()
            case '7':
                while True:
                    certeza = input('Tem certeza que deseja deletar sua conta?\n1-Sim\n2-Não\n\n: ')
                    if certeza != '1' and certeza != '2':
                        print ('Digite apenas 1 ou 2!')
                        continue
                    else: break
                match certeza:
                    case '1':
                        cursor.execute(f'UPDATE horariosDisponiveis SET Status = "Disponível" WHERE cliente = "{email}"')
                        conexao.commit()
                        cursor.execute(f'UPDATE horariosDisponiveis SET cliente = "" WHERE cliente = "{email}"')
                        conexao.commit()
                        cursor.execute(f'DELETE FROM HoraMarcada WHERE email_Paciente = "{email}"')
                        conexao.commit()
                        cursor.execute(f'DELETE FROM Login WHERE email = "{email}"')
                        conexao.commit()
                    case '2':
                        print('Voltando ao Menu...')
                        menu()
            case '8':
                exit()
    menu()
    cursor.close()
    conexao.close()