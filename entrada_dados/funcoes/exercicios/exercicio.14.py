def consumo_combustivel():
    distancia = float(input("Digite a distância percorrida (km): "))
    combustivel = float(input("Digite a quantidade de combustível gasta (L): "))
    consumo = distancia / combustivel
    print(f"Consumo médio: {consumo:.2f} km/L")

consumo_combustivel()