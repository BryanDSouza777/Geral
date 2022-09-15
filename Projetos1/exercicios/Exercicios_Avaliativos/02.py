anon = int(input("Digite o ano que você nasceu: "))
anoa = int(input("Digite o ano atual: "))

anos = anoa - anon
meses = anos * 12 
semanas = meses * 4
dias = meses * 30

anos = print(f'\nVocê tem {anos} anos de idade')
print(f'\nVocê tem {meses} meses de idade')
print(f'\nVocê tem {dias} dias de idade')
print(f'\nVocê tem {semanas} semanas de idade')