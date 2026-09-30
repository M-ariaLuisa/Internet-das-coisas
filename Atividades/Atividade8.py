#Crie uma lista vazia. Use while True para cadastrar notas até que o usuário digite -1 . Depois do
#encerramento, utilize um for para mostrar cada nota cadastrada. Exiba também a quantidade, a
#média, a maior nota, a menor nota e as notas em ordem decrescente.

notas = []

while True:
    nota = float(input("Digite uma nota (-1 para encerrar): "))

    if nota == -1:
        break

    notas.append(nota)

print("\nNotas cadastradas:")

for nota in notas:
    print(nota)

print(f"\nQuantidade de notas: {len(notas)}")
print(f"Média: {sum(notas) / len(notas):.2f}")
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")

notas.sort(reverse=True)

print(f"Notas em ordem decrescente: {notas}")
