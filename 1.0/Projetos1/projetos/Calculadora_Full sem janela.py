n1 = float(input('Digite um numero \n \n'))
operação = (input("Qual a operação?\n\n+ = Soma\n- = Subtração\n* = Multiplicação\n/ = Divisão\n\n"))
n2 = float(input('\nDigite outro numero \n \n'))

if(operação == "+"): (print("\nO resultado é:", n1 + n2))

elif(operação == "-"): (print("\nO resultado é:", n1 - n2))

elif(operação == "*"): (print("\nO resultado é:", n1 * n2))

elif(operação == "/"): (print("\nO resultado é:", n1 / n2))

exit = (input("Precione 'ENTER' para fechar o aplicativo."))