import math
import pyautogui

x1 = 6.752

print(math.ceil(x1))
print(math.floor(x1))

frase = 'quero ser UM programador'

#Texto Maiúsculo
print(frase.upper())
#Texto Minusculo
print(frase.lower())
#Pruneira letra maiúscula
print(frase.capitalize())
#Primeira Letra Maiúscula
print(frase.title())
#Remove espaço em branco
print(frase.strip())
#contar total de caracteres
len(frase) > 50
#seperar
frase.split('UM')
#

#ConCatera
x = 0
y = 72

print ('Minha idade é:', x, y)
print ("minha idade é: {} {}".format(x, y))
print (f'minha idade é {x} {y}')

while x < 5:
    print('Estou dentro do laço')
    print(x)
    x += 1
    if x == 5:
        break

print("Jovem","Programador", sep="-",end="")

string = 'Jovem Programador é legal'
lista = string.split(' ')
lista2 = string.split(',')
print('lista',lista)
print('lista 2',lista2)
for i in lista:
    print(f'A palavra {i} apareceu {lista.count(i)}x na frase!')

    listona = ['O', 'Brasil','ta','com','deficit','na','area','de','programação']
    frase = " ".join(listona)
    print(frase)

matriz = [
    [1,2],
    [3,4],
    [4,5],    
]
for i in matriz:
    print(matriz[0])

lista = ['Joao','Tiago','Paulo','1','2','3','4']
n1, n2, n3, *outra_lista = lista
print(n1, n2, n3, outra_lista)

loggedUser = True
if loggedUser:
    msg = 'Usuario Logado'
else:
    msg = 'Usuario precisa estar logado'
    
msg = 'Usuario Logou' if loggedUser else 'Usuario precisa Logar'
print("Ternario:",msg)
idade =119
msg2 = "Velho"