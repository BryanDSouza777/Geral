while True:
    try:
        paes = int(input("Digite quantos pães você vendeu: "))
        broas = int(input("\nDigite quantas broas você vendeu: "))
        valorpao = float(input("\nDigite o valor dos seus pães: "))
        valorbroa = float(input("\nDigite o valor de suas broas: "))
    except:
        print("\nDigite apenas valores numeros.")

    if valorpao < 0.16 or valorbroa < 1.51:
        print("\nVocê esta vendendo muito parado, não vai haver lucro assim.")
        continue
    else:
        print(" ")
        break

if paes == 0 or valorpao == 0:
    print("\nVocê não teve lucro com os pães.")
else:
    print(f"\nVocê lucrou R$ {(0.12*paes):.2f} com pães.")

if broas == 0 or valorbroa == 0:
    print("\nVocê não teve lucro com os pães.")
else:
    print(f"\nVocê lucrou R$ {(1.50*broas):.2f} com broas.")

print(f"\nLucro Total: R$ {((paes*0.12)+(broas*1.50)):.2f}")

total = (paes*valorpao) + (broas*valorbroa)
print(f'\nSeu total é de R$ {(total):.2f}')
print(f'\nSua reserva é de R$ {(total * 0.10):.2f}')