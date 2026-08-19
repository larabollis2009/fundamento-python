def maior_numero():
    maior = None

    while True:
        numero = float(input("Digite um número: "))

        if maior is None or numero > maior:
            maior = numero

        continuar = input("Deseja continuar? (s/n): ").lower()

        if continuar != "s":
            break

    return maior


resultado = maior_numero()

print("Maior número:", resultado)
