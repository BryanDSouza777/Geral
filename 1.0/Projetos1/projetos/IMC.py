

peso = float(input("Digite seu peso"))
altura = float(input("Digite sua altura"))
imc = peso/((altura)**2)

if imc < 18.5:
    print(f'Seu IMC é de {imc:,.2f}, você está em subpeso.')

elif imc >= 18.5 and imc <= 24.99:
    print (f'Seu IMC é de {imc:,.2f}, você está com o peso normal.')

elif imc >= 25 and imc <= 29.99:
    print (f'Seu IMC é de {imc:,.2f}, você está em sobrepeso.')

else:
    print (f'Seu IMC é de {imc:,.2f}, você está com obesidade.')