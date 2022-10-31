while True:
    print('##### Faça seu cadastro #####\n')
    loginc = str(input("\nCadastre seu username\n\n"))
    senhac = str(input("\nCadastre sua senha\n\n"))

    if loginc == senhac:
        print("Seu username não pode ser igual a senha")
        continue

    if loginc and senhac != str(""):
        print("\nCadastro feito com sucesso\n")
        break

    elif loginc or senhac == str(""):
        print("\nSeu username/senha são inválidos\n")
        continue

while True:
    print('Faça login\n')

    login = str(input("Digite seu username\n\n"))
    senha = str(input("\nDigite sua senha\n\n"))

    if login == loginc and senha == senhac:
        print('\n##### Login feito com Sucesso #####')
        break

    elif login != loginc and senha != senhac:
        print('\n##### Nome de Username/Senha incorreto #####')
        continue