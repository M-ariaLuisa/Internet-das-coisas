#Crie uma lista vazia. Utilize for com range(5) para pedir cinco produtos ao usuário e adicionar
#cada um com append() . Ao final, exiba a lista completa e a quantidade de produtos cadastrados.

produtos = []
for i in range(5):
    produto = input("Digite o nome do produto:")
    produtos.append(produto)
    print("Lista de produtos:",produtos)
print("Quantidade de produtos cadastrados:", len(produtos))
