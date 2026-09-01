def encontrar_produto(produtos, produto):
    return produtos.index(produto)

produtos = ["Mouse", "Teclado", "Monitor", "Camera"]

produto = input("Digite o produto que deseja encontrar: ")

print("Posição:", encontrar_produto(produtos, produto))