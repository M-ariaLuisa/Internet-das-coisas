carrinho = []

while True:
    produto = float(input('Digite o valor do produto: '))
    if produto == 0:
        break
    else:
        carrinho.append(produto)

total = sum(carrinho)
print(f'Total da compra: R${total:.2f}')

#while serve para criar um loop infinito, ou seja, um loop que nunca termina. No caso do exemplo acima, o loop só termina quando o usuário digita 0.