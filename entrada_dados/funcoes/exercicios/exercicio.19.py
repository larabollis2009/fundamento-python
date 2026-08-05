def conta_energia():
    consumo = float(input("Digite o consumo em kWh: "))
    preco_kwh = float(input("Digite o preço do kWh: "))
    total = consumo * preco_kwh
    print(f"Valor da conta de luz: R$ {total:.2f}")

conta_energia()