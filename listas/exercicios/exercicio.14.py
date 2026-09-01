def adicionar_produtos(compras, produtos):
    compras.extend(produtos)
    return compras


def cancelar_compra(compras, produto):
    compras.remove(produto)
    return compras

compras = ["Arroz", "Feijão", "Leite"]
produtos = ["Pão", "Café", "Açúcar"]

adicionar_produtos(compras, produtos)

print("Lista de compras:", compras)

produto = input("Digite o produto que deseja cancelar: ")

print("Lista atualizada:", cancelar_compra(compras, produto))