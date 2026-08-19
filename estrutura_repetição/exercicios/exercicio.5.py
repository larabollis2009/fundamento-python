def tabuada(numero):
    for valor in range(1, 11):
        print(f"{numero} x {valor} = {numero * valor}")

numero = int(input("Digite um número: "))
tabuada(numero)
