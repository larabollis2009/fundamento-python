def contagem_regressiva(numero):
    for valor in range(numero, -1, -1):
        print(valor)

numero = int(input("Digite um número: "))
contagem_regressiva(numero)
