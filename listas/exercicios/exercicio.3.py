def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    print(convidados)

convidados = ["Lara", "Ana"]

novos_convidados = ["João", "Pedro", "Maria"]

adicionar_convidados(convidados, novos_convidados)