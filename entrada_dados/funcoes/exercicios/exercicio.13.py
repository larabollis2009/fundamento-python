def salario_comissao():
    salario_fixo = float(input("Digite o salário fixo: "))
    vendas = float(input("Digite o valor total das vendas: "))
    percentual = float(input("Digite a % de comissão: "))

    comissao = vendas * (percentual / 100)
    salario_final = salario_fixo + comissao

    print(f"Salário final: R$ {salario_final:.2f}")

salario_comissao()
