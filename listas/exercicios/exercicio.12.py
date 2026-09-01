def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    return media

notas = [7, 8, 9, 6]

print("Média:", calcular_media(notas))