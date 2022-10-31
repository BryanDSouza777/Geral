def soma (x,y,z):
    print ('\nResultado:',x+y+z)

n = []
for i in range(3):
    a = float(input("Digite um numero: "))
    n.append(a)
soma(n[0],n[1],n[2])