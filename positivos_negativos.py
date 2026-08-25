#numeros positivos e negativos
positivos = []
negativos = []
for x in range(10):
    num = int(input(f'Digite o número {x + 1}: '))
    if num >= 0:
        positivos.append(num)
    else:
        negativos.append(num)

quantidade_positivos = len(positivos)
print("Quantidade de números positivos:", quantidade_positivos)
quantidade_negativos = len(negativos)
print("Quantidade de números negativos:", quantidade_negativos)
print("Números positivos:", positivos)
print("Números negativos:", negativos)
soma_positivos = sum(positivos)
print("Soma dos números positivos:", soma_positivos)

