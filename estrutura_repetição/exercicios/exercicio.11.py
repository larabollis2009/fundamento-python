def fatorial(numero):
    resultado = 1

    for valor in range(1, numero + 1):
        resultado *= valor

    return resultado


numero = int(input("Digite um número: "))

resultado = fatorial(numero)

print("Fatorial:", resultado)
