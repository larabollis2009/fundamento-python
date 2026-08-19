def eh_primo(numero):
    if numero < 2:
        return False

    for valor in range(2, numero):
        if numero % valor == 0:
            return False

    return True


numero = int(input("Digite um número: "))

resultado = eh_primo(numero)

print(resultado)
