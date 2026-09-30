#Crie uma lista vazia e utilize while True para receber nomes.
# Cada nome deve ser incluído com append() .
#  Quando o usuário digitar 'fim' , encerre com break .
# Depois, organize os nomes em ordem alfabética e mostre a lista e sua quantidade.

nomes = []
while True:
    nome = input("Digite um nome (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break
    nomes.append(nome)

nomes.sort()
print("Nomes em ordem alfabética:", nomes)
print("Quantidade de nomes:", len(nomes))