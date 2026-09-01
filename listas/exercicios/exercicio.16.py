def criar_ranking(pontuacoes):
    return sorted(pontuacoes, reverse=True)

pontuacoes = [50, 90, 70, 100, 60]

print("Ranking:", criar_ranking(pontuacoes))