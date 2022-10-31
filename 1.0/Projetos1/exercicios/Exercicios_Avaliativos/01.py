#1. Faça um algoritmo que calcule e mostre a tabuada de um numero digitado pelo usuário
try:
    n1 = float(input("Digite um numero para ver sua tabuada."))
    limite = int(input("Digite até onde você deseja que sua tabuada vá."))
except:
    print("Digite apenas números")
for i in range(limite+1):
    x=n1 * i
    print(f'{n1} x {i} = {x}')
