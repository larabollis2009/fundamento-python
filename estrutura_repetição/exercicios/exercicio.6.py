def somar_ate(numero):
    soma = 0

    for valor in range(1, numero + 1):
        soma += valor

    return soma

numero = int(input("Digite um número: "))
resultado = somar_ate(numero)

print("Soma:", resultado)
