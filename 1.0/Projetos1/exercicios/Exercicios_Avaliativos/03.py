#3.João recebeu seu salário de R$1200,00 e precisa pagar duas contas(C1=R$200,00 e C2=R$120,00)
# que estão atrasadas.Como as contas estão atrasadas,João terá de pagar multa de 2% sobre cada conta.
# Faça um algoritmo que calcule e mostre quanto restará do salário do João
salario = 1200.00
c1 = 200.00
c2 = 120.00

print(f'\nVocê pagará R$ {(c1+(c1*0.02)):.2f} na 1° conta atrasada.')
print(f'\nVocê pagará R$ {(c2+(c2*0.02)):.2f} na 2° conta atrasada.')
dividat = (c1*0.02)+(c2*0.02)
print(f'\nVocê pagará R$ {c1*0.02:.2f} e R$ {c2*0.02:.2f}, como multa.\nTotal de R$ {dividat:.2f} pago de multa.')
print(f'\nSobrou R$ {(salario - dividat):.2f} do seu salário.')