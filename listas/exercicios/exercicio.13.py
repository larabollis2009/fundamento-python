def adicionar_cliente(fila, cliente):
    fila.append(cliente)


def atender_cliente(fila):
    if len(fila) > 0:
        return fila.pop(0)
    else:
        return "Não há clientes na fila"


fila = []

while True:
    cliente = input("Digite o nome do cliente ou 'sair' para terminar: ")

    if cliente.lower() == "sair":
        break

    adicionar_cliente(fila, cliente)

print("Fila:", fila)

cliente_atendido = atender_cliente(fila)

print("Cliente atendido:", cliente_atendido)
print("Fila atualizada:", fila)