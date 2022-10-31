from quadrado import Quadrado
lado = float(input("Digite o tamanho do lado do quadrado."))

q1 = Quadrado(lado)
q2 = Quadrado(5)

print (q1.calcular())

trocar = input('\nDeseja mudar o tamanho do lado?\nS = sim\nN = não\n\n')
trocar = trocar.upper()
if trocar == "S":
    lado = float(input('\nTamanho do lado: '))
print('')
q1.mudarLado(lado)
    
print(q1.calcular())