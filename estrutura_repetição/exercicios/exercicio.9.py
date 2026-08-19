def contar_pares(inicio, fim):
    quantidade = 0

    for valor in range(inicio, fim + 1):
        if valor % 2 == 0:
            quantidade += 1

    return quantidade


inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

resultado = contar_pares(inicio, fim)

print("Quantidade de números pares:", resultado)
