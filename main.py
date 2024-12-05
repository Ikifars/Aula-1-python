Ceara = (3, 2, 2)

media = sum(Ceara) / len(Ceara)

print("A média do ceará é:", media)

Capital_do_ceara = (1, 1, 0)

media = sum(Capital_do_ceara) / len(Capital_do_ceara)

print("A média desse timinho é", media)

# Pontuações das equipes
pontuacoes = []

# Recebendo a pontuação de cada equipe
Ceara= float(input("Digite a pontuação da equipe 1: "))
Capital_do_ceara = float(input("Digite a pontuação da equipe 2: "))

# Adicionando as pontuações na lista
pontuacoes.append(Ceara)
pontuacoes.append(Capital_do_ceara)

# Ordenando as pontuações em ordem crescente
pontuacoes.sort()

# Exibindo as pontuações em ordem crescente
print("Pontuações em ordem crescente:", pontuacoes)
