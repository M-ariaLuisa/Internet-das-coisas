#Peça seis números inteiros utilizando um laço for e armazene-os em uma lista.
# Depois, mostre a soma, o maior valor, o menor valor e os números em ordem crescente.

numeros = []
for i in range(6):
    numero = int(input("Digite um número inteiro:"))
    numeros.append(numero)
print("Soma de números:" , sum(numeros))
print("Maior número:" , max(numeros))
print("Menor número:", min(numeros))
numeros.sort()
print("Números em ordem crescente:", numeros)

