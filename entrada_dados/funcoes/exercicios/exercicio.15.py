def idade_meses_dias():
    idade = int(input("Digite a idade em anos: "))
    meses = idade * 12
    dias = idade * 365
    print(f"Idade em meses: {meses}")
    print(f"Idade em dias (aprox.): {dias}")

idade_meses_dias()