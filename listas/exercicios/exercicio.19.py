def adicionar_nota(notas, nota):
    notas.append(nota)


def inserir_nota(notas, nota, posicao):
    notas.insert(posicao, nota)


def adicionar_varias_notas(notas, novas_notas):
    notas.extend(novas_notas)


def remover_nota(notas, nota):
    notas.remove(nota)


def remover_ultima(notas):
    return notas.pop()


def encontrar_nota(notas, nota):
    return notas.index(nota)


def quantidade_notas(notas):
    return len(notas)


def ordenar_notas(notas):
    return sorted(notas)


def notas_inversas(notas):
    return list(reversed(notas))


def soma_notas(notas):
    return sum(notas)


def media_turma(notas):
    return sum(notas) / len(notas)


notas = [7.5, 6.0, 8.5, 9.0, 5.5]

# 1. Adicionar uma nota
adicionar_nota(notas, 8.0)

# 2. Inserir uma nota
inserir_nota(notas, 7.0, 2)

# 3. Adicionar várias notas
adicionar_varias_notas(notas, [6.5, 9.5])

# 4. Remover uma nota
remover_nota(notas, 5.5)

# 5. Remover a última nota
removida = remover_ultima(notas)

# 6. Encontrar posição de uma nota
posicao = encontrar_nota(notas, 8.5)

# 7. Quantidade de notas
quantidade = quantidade_notas(notas)

# 8. Ordenar notas
ordenadas = ordenar_notas(notas)

# 9. Ordem inversa
inversas = notas_inversas(notas)

# 10. Soma
soma = soma_notas(notas)

# 11. Média
media = media_turma(notas)

print("Notas:", notas)
print("Nota removida:", removida)
print("Posição da nota 8.5:", posicao)
print("Quantidade de notas:", quantidade)
print("Notas ordenadas:", ordenadas)
print("Notas em ordem inversa:", inversas)
print("Soma das notas:", soma)
print("Média da turma:", media)