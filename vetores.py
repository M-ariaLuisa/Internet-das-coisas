numeros = [33,11,22,54,51,52,17]
nomes = ['Julia', 'Maria', 'Luiza', 'Enzo']

numeros.append(67)
numeros.insert(3, 50)
numeros.pop(0)
numeros.remove(54)
nomes.remove('Enzo')

print(numeros)
print(nomes)
#append adiciona um elemento ao final da lista
#insert adiciona um elemento em uma posição específica da lista
#pop remove um elemento da lista, podendo ser especificado o índice do elemento a ser removido
#remove remove um elemento da lista, sendo necessário informar o valor do elemento a ser removido