class Matematica:
    def __init__(self,nome):
        self.nome = nome
    def calculo(self,n1,x,el,op,n2,n):
        self.n1 = n1
        self.x = x
        self.el = el
        self.op1 = op
        self.n2 = n2
        self.n = n
        print(f'{n1:.0f}.{x:.0f} {op[0]} {n2:.0f}.{x:.0f} {op[1]} {n:.0f}')

        calcular = {"+":(n1*(x**el)) + (n2*x), "-":(n1*(x**el)) - (n2*x), "*":(n1*(x**el)) * (n2*x), "/":(n1*(x**el)) / (n2*x)}
        y = calcular[op[0]]
        calcular2 = {"+":y + n, "-":y - n, "*":y * n, "/":y / n}
        total = calcular2[op[1]]
        return total
nome = input('Digite seu nome: ')
nome += ','
mat = Matematica(nome)
x1 = float(input('Digite o f(x): '))
n1 = float(input('Digite o 1° número: '))
try:
    el = int(input('O 1° "x" é elevado a algo? Se sim qual?\n\nSe não aperte "Enter"'))
except:
    el = 1
if el != float:
    el == 1
elif el == '':
    el == 1
op = input('Digite o(s) sinal(is): ')
n2 = float(input('Digite o 2° número: '))
n3 = float(input('Digite o 3° número: '))
print (mat.nome,'o resultado é:',mat.calculo(n1,x1,el,op,n2,n3))