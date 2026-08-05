def valor_prestacao():
    preco = float(input("Digite o valor total do produto: "))
    parcelas = int(input("Digite a quantidade de parcelas: "))
    valor_parcela = preco / parcelas
    print(f"Cada parcela será de: R$ {valor_parcela:.2f}")

valor_prestacao()