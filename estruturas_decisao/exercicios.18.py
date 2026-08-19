def calcular_frete():
    valor_compra = float(input("Digite o valor da compra: R$ "))

    if valor_compra <= 100:
        frete = 20
    elif valor_compra <= 300:
        frete = 10
    else:
        frete = 0

    valor_total = valor_compra + frete

    print("Frete: R$", frete)
    print("Valor total: R$", valor_total)

calcular_frete()