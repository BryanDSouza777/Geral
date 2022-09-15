palavra = str(input("Digite alguma Palavra\n\n"))
vogal = ['a','e','i','o','u']

if palavra[-1] in vogal:
    print("\nEssa palavra tem a terminação de uma Vogal")

else:
    print("\nEssa palavra tem a terminação de uma consoante")