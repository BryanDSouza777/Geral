from operator import and_
import random
from rpg import Personagem
nome = input('Digite seu nome: ')
def setRace():
    raça = int(input('\nSelecione sua raça:\n\n1-Anões\n2-Draconatos\n3-Elfos\n4-Gnomos\n5-Halflings\n6-Humanos\n7-Kor\n8-Meio-Orc\n9-Replicante\n10-Tieflings\n11-Tritão\n\nResposta: '))
    return raça
while True:
    match setRace():
        case 1:
            raça = 'Anões'
            break
        case 2:
            raça = 'Draconatos'
            break
        case 3:
            raça = 'Elfos'
            break
        case 4:
            raça = 'Gnomos'
            break
        case 5:
            raça = 'Halflings'
            break
        case 6:
            raça = 'Humanos'
            break
        case 7:
            raça = 'Kor'
            break
        case 8: 
            raça = 'Meio-Orc'
            break
        case 9:
            raça = 'Replicante'
            break
        case 10:
            raça = 'Tieflings'
            break
        case 11:
            raça = 'Tritão'
            break
        case _:
            print('Seleção de raça obrigatoria')
            continue
def setClass():
    classe = int(input('\nSelecione sua classe:\n\n1-Bárbaro\n2-Bardo\n3-Bruxo\n4-Clérigo\n5-Druida\n6-Feiticeiro\n7-Guardião\n8-Guerreiro\n9-Ladino\n10-Mago\n11-Monge\n\nResposta: '))
    return classe
while True:
    match setClass():
        case 1:
            classe = 'Bárbaro'
            break
        case 2:
            classe = 'Bardo'
            break
        case 3:
            classe = 'Bruxo'
            break
        case 4: 
            classe = 'Clérigo'
            break
        case 5:
            classe = 'Druida'
            break
        case 6:
            classe = 'Feiticeiro'
            break
        case 7:
            classe = 'Guardião'
            break
        case 8: 
            classe = 'Guerreiro'
            break
        case 9:
            classe = 'Ladino'
            break
        case 10:
            classe = 'Mago'
            break
        case 11:
            classe = 'Monge'
            break
        case _:
            print('Seleção de classe obrigatoria')
            continue

ps = Personagem(nome,raça,classe)
ab = []
for i in range(6):
    listrd = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    menor = min(listrd)  
    listrd.remove(menor)
    i += random.randint(1,6)
    soma = sum(listrd)
    ab.append(soma)
ps.atributos(ab[0],ab[1],ab[2],ab[3],ab[4],ab[5])
ps.skillsraça(ps.raça)
ps.skillclasse(ps.classe)
print(f'\nClasse: {ps.classe}')
print(f'Raça: {raça}\n')
ps.mostrarAtri()
ps.mostrarProf()
while True:
    verDesc = int(input(f'\nDeseja ver a descrição da sua:\n1 - Raça\n2 - Classe\n3 - Ambos\n4 - Sair\n\nResposta: '))
    match verDesc:
        case 1:
            ps.mostrarDescRaça()
            verDesc1 = int(input(f'\nDeseja repetir?\n1 - Sim\n2 - Não\n\nResposta: '))
            match verDesc1:
                case 1:
                    continue
                case 2:
                    break
        case 2:
            ps.mostrarDescClasse()
            verDesc1 = int(input(f'\nDeseja repetir?\n1 - Sim\n2 - Não\n\nResposta: '))
            match verDesc1:
                case 1:
                    continue
                case 2:
                    break
        case 3:
            ps.mostrarDescRaça()
            ps.mostrarDescClasse()
            verDesc1 = int(input(f'\nDeseja repetir?\n1 - Sim\n2 - Não\n\nResposta: '))
            match verDesc1:
                case 1:
                    continue
                case 2:
                    break
        case 4:
            break
        case _:
            print('Digite apenas 1, 2 ou 3.')
            continue