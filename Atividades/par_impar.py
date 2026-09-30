#numeros pares e impares

pares = []
impares = []

for x in range(10):
    num = int(input(f'Digite o número {x + 1}: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')