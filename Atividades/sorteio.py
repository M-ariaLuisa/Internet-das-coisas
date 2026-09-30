#programa com o objetivo de sortear um nome entre 10

import random,os

nomes = []
for x in range(10):
    nome = input(f'Digite o nome {x + 1}: ')
    nomes.append(nome)
    os.system('cls' or 'clear')  # Limpa a tela após cada entrada
sorteado = random.choice(nomes)
print(f'O nome sorteado foi: {sorteado}')
