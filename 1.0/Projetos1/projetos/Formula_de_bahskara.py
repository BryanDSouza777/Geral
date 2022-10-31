a = float(input("Digite o numero 'a' de sua formula\n\n"))
b = float(input("\nDigite o numero 'b' de sua formula\n\n"))
c = float(input("\nDigite o numero 'c' de sua formula\n\n"))

delta = ((b**2) - (4*a*c))**(1/2)
x1 = (-(b) + delta)/(2*a)
x2 = (-(b) - delta)/(2*a)

print("delta =",delta)
print("x1 =",x1)
print("x2 =",x2)