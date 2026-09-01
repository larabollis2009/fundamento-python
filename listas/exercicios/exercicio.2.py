def inserir_aluno(alunos, nome, posicao):
    alunos.insert(posicao, nome)
    print(alunos)

alunos = ["Thayna", "Milena", "Maria"]

nome = input("Digite o nome do aluno: ")
posicao = int(input("Digite a posicao :"))

inserir_aluno(alunos, nome, posicao)