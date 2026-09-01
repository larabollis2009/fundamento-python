def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é {nome}")


lista_de_nomes = ["Guilherme", "Lara", "Ferraz", "Pimenta"]

mostrar_nomes(lista_de_nomes)


# Adicionando novo nome na lista
def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)


adicionar_nome(lista_de_nomes, "Nicoly")


# Adicionando novo nome em uma posição específica
def adicionar_nome_posicao(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f"O nome {nome} foi inserido na posição {posicao} da lista: {nomes}")


adicionar_nome_posicao(lista_de_nomes, "Guilherme", 2)


# Juntando duas listas
def juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f"Os novos nomes {novos_nomes} foram inseridos na lista: {nomes}")


novos_nomes = ["Francisco", "Nilton"]

juntar_nomes(lista_de_nomes, novos_nomes)


# Removendo itens da lista pelo valor
def remover_nome_pelo_valor(nomes, nome):
    nomes.remove(nome)
    print(f"O nome {nome} foi removido da lista: {nomes}")


remover_nome_pelo_valor(lista_de_nomes, "Pimenta")


# Removendo nome pelo índice
def remover_nome_pelo_indice(nomes, posicao):
    nome_removido = nomes[posicao]
    nomes.pop(posicao)
    print(f"O nome da posição {posicao} era {nome_removido} e foi removido.")
    print(f"Lista atualizada: {nomes}")


remover_nome_pelo_indice(lista_de_nomes, 4)


# Descobrindo a posição (index) pelo nome
def encontrar_posicao_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Nome não encontrado!")
    else:
        posicao = nomes.index(nome)
        print(f"A posição do nome {nome} é {posicao}")


encontrar_posicao_pelo_valor(lista_de_nomes, "Guilherme")


# Contando elementos da lista
def quantidade_de_nomes(nomes):
    quantidade = len(nomes)
    print(f"A quantidade de nomes da lista é {quantidade}")


quantidade_de_nomes(lista_de_nomes)


# Ordenando os elementos da lista
def ordenar_nomes(nomes):
    lista_de_nomes_ordenados = sorted(nomes)
    print(f"A lista ordenada é {lista_de_nomes_ordenados}")


ordenar_nomes(lista_de_nomes)


# Operações matemáticas
# Calcular média
def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    print(f"A média das notas é {media}")


notas_semestre = [7.8, 6.5, 9, 8.7, 9.5]
calcular_media(notas_semestre)


def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    ordenadas = sorted(notas)

    media = sum(notas) / len(notas)

    return ordenadas, media


notas_oredenadas, batata = gerenciar_notas(notas_semestre, 3.5)
print(f"notas oredenadas = {notas_oredenadas}")
print(f" A média das notas é {batata}")


# Lista d listas

def adicionr_produto(produto, produtos):
    produto.append(produto)
    print(f"Minha lista de produto {produto[0]}")


lista_produto = [
    ["Arroz", 2, 32.00],
    ["Feijão", 3, 8.50],
]

novo_produto = ["Café", 2, 28.0]
adicionar_produto(lista_produto, novo_produto)

