#programa que organize uma lista de nomes em ordem alfabetica

nomes = []
for x in range(5):
    nome = input(f'Digite o nome {x + 1}: ')
    nomes.append(nome)

nomes.sort()
print(f'Lista de nomes em ordem alfabética: {nomes}')
