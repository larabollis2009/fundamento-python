def caixa_eletronico(valor):
    notas = [100, 50, 20, 10, 5, 2]

    for nota in notas:
        quantidade = valor // nota

        if quantidade > 0:
            print(f"{quantidade} nota(s) de R$ {nota}")

        valor = valor % nota


valor = int(input("Digite o valor para saque: "))

if valor > 0:
    caixa_eletronico(valor)
else:
    print("Digite um valor válido.")
