from termios import B4000000


def reset():

    #importar
    from tkinter.tix import ButtonBox
    import requests
    import tkinter
    import pyautogui 
    import keyboard
    
    #Cores
    cor1 = "#1e1f1e" #Preto
    cor2 = "#3c3540" #Cinza Azulado
    cor3 = "#e3e3e3" #Cinza Claro
    cor4 = "#ff4000" #Laranja

    #Janela
    janela = tkinter.Tk()
    janela.title('Calculadora')
    janela.geometry('235x318')
    janela.config (bg=cor1)

    #Frames
    tkinter.frame=tkinter.Frame(janela, width=235, height=50, bg=cor2)
    tkinter.frame.grid(row=0, column=0)

    framec=tkinter.Frame(janela, width=235, height=268, bg=cor3)
    framec.grid(row=1, column=0)

    #Botões
    b1 = tkinter.Button(framec, text = "C", width=11, height=2, bg=cor4, font=('Ivy 13q bold'), relief=RAISED)
    b1.place (x=0, y=0)
    
    b2 = tkinter.Button(framec, text = "%", width=11, height=2, bg=cor4)
    b2.place (x=86, y=0)
    
    b3 = tkinter.Button(framec, text = "÷", width=8, height=2, bg=cor4)
    b3.place (x=172, y=0)
    
    b4 = tkinter.Button
    b4.place (x=, y=)

    janela.mainloop()
    
    #Variaveis
    vi= float(input("Digite um Valor.\n\n"))
    pi = float(input("\nDigite a porcentagem que sera aplicada.\n\n"))
    op = (input("\nA porcentagem que sera aplicada sera\n+ = Crescente\n- = Decrescente\n\n"))

    #Calculos
    positivo = float(vi*(1 +(pi/100)))
    negativo = float(vi*(1 -(pi/100)))

    #Main
    if (op == '+'): print("\nSeu novo valor é: R$", positivo,", com o valor de R$", positivo - vi, "acrescentado")

    elif (op == '-'): print("\nSeu novo valor é: R$", negativo,", com o valor de R$", negativo - vi, "descontado")

    else: print("\nVocê digitou algo errado!")
    
    restart = (input("\nDigite 'again' para reiniciar\n\n")).lower()
    if restart == ("again"):
        print("\nReiniciando...\n")
        reset()
 
    else:
        exit()
        
reset()