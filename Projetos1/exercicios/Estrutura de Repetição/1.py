while True:
    n1 = float(input("Digite um numero de 0 à 10\n\n"))

    if n1 >= 0 and n1 <= 10:
        print ("\nNumero Valido")
        break

    elif n1 < 0 and n1 > 10:
        print("\nNumero invalido")  
        pass