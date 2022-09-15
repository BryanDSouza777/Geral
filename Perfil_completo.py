nome = str(input("Digite seu nome"))
idade = int(input("Digite sua idade"))
altura = float(input("Digite sua altura"))
peso = float(input("Digite seu peso"))

anoatual = 2022
aniversario = str(input("Você ja fez aniversario este ano?\n\ns = sim\nn = não"))

if aniversario == 's' or aniversario == 'S':
    print(f'Você nasceu em {anoatual - idade}')

elif aniversario == 'n' or aniversario == 'N':
    print(f'Você nasceu em {anoatual - idade - 1}')

imc = peso/((altura)**2)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}, você está em subpeso.')

elif imc >= 18.5 and imc <= 24.99:
    print (f'Seu IMC é de {imc:.2f}, você está com o peso normal.')

elif imc >= 25 and imc <= 29.99:
    print (f'Seu IMC é de {imc:.2f}, você está em sobrepeso.')

else:
    print (f'Seu IMC é de {imc:.2f}, você está com obesidade.')