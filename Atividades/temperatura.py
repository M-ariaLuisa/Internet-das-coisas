temperatura = []

for x in range(5):
    temp = float(input(f'Digite a temperatura {x + 1}: '))
    temperatura.append(temp)

media = sum(temperatura) / len(temperatura)
menor = min(temperatura)
maior = max(temperatura)

print(f'A média das temperaturas é: {media:.1f}°C')
print(f'A menor temperatura é: {menor:.2f}°C')
print(f'A maior temperatura é: {maior:.2f}°C')