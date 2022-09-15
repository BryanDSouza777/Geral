while True:
    try:
        cavalos=int(input("Quantos cavalos você tem no seu haras?\n\n"))
    except:
        print("\nDigite apenas a quantidade de cavalos. (Número Inteiro)")
    if cavalos == 0:
        print("\nVocê não tem cavalos.")
    else:
        print(f'\nVocê tem que comprar {cavalos*4} ferraduras para seus cavalos.')
        break