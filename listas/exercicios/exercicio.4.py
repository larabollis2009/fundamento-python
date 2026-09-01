def inserir_aluno(alunos, nome, posicao ):
    alunos.insert(posicao, nome)
    print(alunos)

alunos = ["ana", "carlos", "joao"]

nome = input("Digite o nome do aluno: ")
posicao = int(input("digite a posicao: "))

inserir_aluno(alunos, nome, posicao)