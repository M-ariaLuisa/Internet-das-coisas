# 2) O Somador Infinito (while True + append)
# Crie um programa que peça números ao usuário indefinidamente.
# Se o usuário digitar 0, o programa para.
# Cada número digitado (exceto o 0) deve ser guardado em uma lista.
# No final, mostre a lista completa e a soma de todos os itens usando sum().

numeros = []
while True:
    num = int(input('Digite o número :'))
    if(num !=0):
        numeros.append(num)
    else:
        break
soma = sum(numeros)
print(f'A soma dos números digitados é: {soma}')
print(f'A lista completa dos números digitados é: {numeros}')