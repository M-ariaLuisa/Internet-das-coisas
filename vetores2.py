numeros = [33,11,22,54,51,52,17]
nomes = ['Julia', 'Maria', 'Luiza', 'Enzo']

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f'Maior número: {maior_numero}')
print(f'Menor número: {menor_numero}') 

#sort serve para ordenar listas, seja de números ou de strings. No caso de números, ele ordena do menor para o maior. No caso de strings, ele ordena em ordem alfabética.
#numeros.sort()
#numeros.reverse()
#print(numeros)

#reverse serve para inverter a ordem da lista, ou seja, do último elemento para o primeiro.
#len serve para contar a quantidade de elementos da lista. No caso de números, ele conta quantos números existem na lista. No caso de strings, ele conta quantas strings existem na lista.
#quantidade = len(numeros)

#count serve para contar quantas vezes um determinado elemento aparece na lista. No caso de números, ele conta quantas vezes um determinado número aparece na lista. No caso de strings, ele conta quantas vezes uma determinada string aparece na lista.
#sum serve para somar todos os elementos da lista. No caso de números, ele soma todos os números da lista. No caso de strings, ele não funciona, pois não é possível somar strings.
total = sum(numeros)
print(f'Soma dos números: {total}')

#max serve para encontrar o maior elemento da lista. No caso de números, ele encontra o maior número da lista. No caso de strings, ele encontra a string que vem por último na ordem alfabética.
#min serve para encontrar o menor elemento da lista. No caso de números, ele encontra o menor número da lista. No caso de strings, ele encontra a string que vem por primeiro na ordem alfabética.