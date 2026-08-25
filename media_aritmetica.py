#programa que solicita ao usuário a nota de 8 alunos
#calcula-se a media aritmetica
#cria outra lista com alunos que ficaram acima da média

notas = []

# Ler as notas dos 8 alunos
for i in range(8):
    nota = float(input(f"Digite a nota do {i + 1}º aluno: "))
    notas.append(nota)

# Calcular a média
media = sum(notas) / len(notas)

print("Média da turma:", media)

# Criar lista com notas acima da média
acima_da_media = []

for nota in notas:
    if nota > media:
        acima_da_media.append(nota)

print("Notas acima da média:", acima_da_media)
