def calcular_salario():
    valor_hora = float(input("Digite quanto ganha por hora: "))
    horas = float(input("Digite a quantidade de horas trabalhadas: "))
    salario = valor_hora * horas
    print(f"Salário total: R$ {salario:.2f}")

calcular_salario()