def eh_primo(numero):
    if numero < 2:
        return False

    for valor in range(2, numero):
        if numero % valor == 0:
            return False

    return True

def mostrar_primos(inicio, fim):
    for numero in range(inicio, fim + 1):
        if eh_primo(numero):
            print(numero)