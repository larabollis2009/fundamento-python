def calcular_imc():
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")

calcular_imc()
