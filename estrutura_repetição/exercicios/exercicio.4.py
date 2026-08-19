def mostrar_impares(numero):
    for valor in range(1, numero + 1):
        if valor % 2 != 0:
            print(valor)

numero = int(input("Digite um número: "))
mostrar_impares(numero)
