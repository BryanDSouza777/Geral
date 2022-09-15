n1 = float(input("Digite um numero: "))
n2 = float(input("\nDigite outro numero: "))

if n1%n2 == 0 or n2%n1 == 0:
    print("\nSão múltiplos")
else:
    print("\nNão são múltiplos")