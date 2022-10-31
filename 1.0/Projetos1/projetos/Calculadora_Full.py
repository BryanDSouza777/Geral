#importar
from tkinter.tix import ButtonBox
import requests
from tkinter import *

#Cores
cor1 = "#1e1f1e" #Preto
cor2 = "#3c3540" #Cinza Azulado
cor3 = "#e3e3e3" #Cinza Claro
cor4 = "#ff4000" #Laranja

#Janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.config (bg=cor1)

#Frames
frame=Frame(janela, width=235, height=50, bg=cor2)
frame.grid(row=0, column=0)

framec=Frame(janela, width=235, height=268, bg=cor3)
framec.grid(row=1, column=0)

#Botões
b1 = Button (framec, text = "%", width=11, height=2, bg=cor4)
b1.place (x=0, y=0)
b2 = Button (framec, text = "C", width=11, height=2, bg=cor4)
b2.place (x=87, y=0)
b3 = Button (framec, text = "back", width=9, height=2, bg=cor4)
b3.place (x=169, y=0)
b4 = Button (framec, text = "7", width=9, height=2, bg=cor4)
b4.place (x=0, y=58)
b5 = Button (framec, text = "8", width=9, height=2, bg=cor4)
b5.place (x=87, y=58)
b6 = Button (framec, text = "9", width=9, height=2, bg=cor4)
b6.place (x=169, y=58)
b7 = Button (framec, text = "4", width=9, height=2, bg=cor4)
b7.place (x=0, y=117)
b8 = Button (framec, text = "5", width=9, height=2, bg=cor4)
b8.place (x=87, y=117)
b9 = Button (framec, text = "6", width=9, height=2, bg=cor4)
b9.place (x=169, y=117)
b10 = Button (framec, text = "1", width=9, height=2, bg=cor4)
b10.place (x=169, y=175)
b11 = Button (framec, text = "2", width=9, height=2, bg=cor4)
b11.place (x=0, y=175)
b12 = Button (framec, text = "3", width=9, height=2, bg=cor4)
b12.place (x=87, y=175)



janela.mainloop()

#Codigo Main
n1 = float(input('Digite um numero \n \n'))
operação = (input("Qual a operação?\n\n+ = Soma\n- = Subtração\n* = Multiplicação\n/ = Divisão\n\n"))
n2 = float(input('\nDigite outro numero \n \n'))


if operação == "+":
    print('\n', n1 + n2)

elif operação == "-":
    print('\n', n1 - n2)

elif operação == "*":
    print('\n', n1 * n2)

elif(operação == "/"):
    print('\n', n1 / n2)
