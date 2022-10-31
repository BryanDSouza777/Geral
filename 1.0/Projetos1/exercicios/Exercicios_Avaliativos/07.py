try:
    n1 = int(input("Digite um numero: "))
except:
    print("\nDigite apenas numeros inteiros.")

soma=[]
soma.append(n1)
if n1 == 1:
    print('1.00')
else:
    for i in range(n1):
        x = (1/(i+2))
        soma.append(x)
    total = sum(soma)
    print (f'{total:.2f}')