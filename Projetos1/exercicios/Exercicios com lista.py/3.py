from tkinter import N


qtd = int(input("Quantas notas deseja você ver a media?"))
notas = []

for i in range(qtd):
    numero = float(input(f"Digite sua {i+1}° nota:\n\n"))
    notas.append(numero)
print (f'Suas notas são: {notas}')
print ('Sua media é:', sum(notas)/qtd)