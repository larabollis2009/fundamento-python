def somar_pares(inicio, fim):
    soma = 0

    for valor in range(inicio, fim + 1):
        if valor % 2 == 0:
            soma += valor

    return soma


inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

resultado = somar_pares(inicio, fim)

print("Soma dos números pares:", resultado)
