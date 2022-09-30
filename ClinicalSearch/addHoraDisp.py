def inserirHorarioMed(nome,tipomed,hora,minuto,intervalos30):
    import sqlite3
    conexao = sqlite3.connect('ClinicalSearch/clinicalsearch.db')
    cursor = conexao.cursor()
    while True:
        diaSemana = input('\n1-Segunda-Feira\n2-Terça-Feira\n3-Quarta-Feira\n4-Quinta-Feira\n5-Sexta-Feira\n6-Sábado\n7-Domingo')
        if diaSemana != '1' and diaSemana != '2' and diaSemana != '3' and diaSemana != '4' and diaSemana != '5' and diaSemana != '6' and diaSemana != '7':
            print('\nDigite um numero de 1 à 7!')
            continue
        else: break
    match diaSemana:
        case '1': diaSemana = 'Segunda-Feira'
        case '2': diaSemana = 'Terça-Feira'
        case '3': diaSemana = 'Quarta-Feira'
        case '4': diaSemana = 'Quinta-Feira'
        case '5': diaSemana = 'Sexta-Feira'
        case '6': diaSemana = 'Sábado'
        case '7': diaSemana = 'Domingo'
    for i in range(intervalos30):
        if minuto > 59:
            minuto = 0
            hora += 1
        if hora < 10:
            hora = f'0{hora}'
        if minuto == 0:
            minuto = '00'
        horario = f'{hora}:{minuto}'
        print (horario)
        cursor.execute('INSERT INTO horariosDisponiveis(nomeMedico,tipoMedico,diaSemana,HorarioDisponivel,Status) VALUES (?,?,?,?,?)',(nome,tipomed,diaSemana,horario,'Disponível'))
        conexao.commit()
        minuto = int(minuto)
        hora = int(hora)
        minuto += 30
    cursor.close()
    conexao.close()