def calculo(n1, op, n2):
    calcular = {"+":n1 + n2, "-":n1 - n2, "*":n1 * n2, "/":n1 / n2, "**":n1 ** n2, "v":n1**(1/n2)}
    return calcular[op]
def reiniciar():
    dsj = input(f'\nDeseja reiniciar?\n\nY = sim\nN = não\n\n')
    dsj = dsj.lower()
    if dsj == 'y':
        print (f'\nReiniciando...\n')
        main()
    elif dsj == 'n':
        print(f'\nEncerrando...\n')
        exit()
    else:
        print('Digite apenas Y ou N')
        reiniciar()
def main():
    n1 = float(input('1° numero\n\n'))
    op = input('\nDigite a operação\n\n+ = soma\n- = subtração\n* = multiplicação\n/ = divisão\n** = exponenciação\nv = raiz\n\n')
    n2 = float(input('\n2° numero\n\n'))
    listop = ['+','-','*','/','**','v']
    if op not in listop:
        print(f'\nERRO !!!\nVerifique se você fez tudo certo!')
        reiniciar()
    calculo(n1,op,n2)
    print(f'\n{calculo(n1,op,n2)}')
    reiniciar()
main()