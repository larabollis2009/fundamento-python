def validar_senha(senha_correta):
    tentativas = 0

    while tentativas < 3:
        senha = input("Digite a senha: ")

        if senha == senha_correta:
            print("Acesso permitido!")
            return

        tentativas += 1
        print("Senha incorreta.")

    print("Acesso bloqueado!")

senha_correta = "1234"

validar_senha(senha_correta)
