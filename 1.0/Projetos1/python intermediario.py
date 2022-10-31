def função():
    print("Ola Jovens!")
função()
função()
função()
função()
#DRY -> Don't Repeat Yourself -> Não repita a sí mesmo
def exibeMsg (msg):
    print (msg)
exibeMsg("Oi")
exibeMsg("10")
exibeMsg("5/2")
def saudacao(msg = "Oi", nome = "Bryan"):
    print(msg, nome)
saudacao("Ola", "Kaua")
saudacao('Bom dia', 'letielli')
saudacao(nome='zezinho')
saudacao(nome='bryan', msg='ola')
saudacao('ola', 'bryan')
saudacao('tudo bem', 'claudio')
saudacao('dboa', 'mano')

#return funciona que nem o break dos laços de repetição, interrompe a execução da função, mas diferente do break, ela retorna um valor quando chamada