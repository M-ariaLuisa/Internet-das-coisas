#Crie uma lista vazia e apresente continuamente o menu: 1 - Adicionar tarefa, 2 - Remover tarefa,
#3 - Mostrar tarefas e 0 - Sair.
#Use w h i l e T r u e para manter o menu ativo, append() para
#adicionar, remove() para retirar e break para encerrar.

tarefas = []

print("Menu de tarefas:")
print("1. Adicionar tarefa")
print("2. Remover tarefa")
print("3. Mostrar tarefas")

while True:
    opcao = input("Escolha a opção desejada: ")
    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        tarefa = input("Digite a tarefa a ser removida: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")
        else:
            print("Tarefa não encontrada.")
    elif opcao == "3":
        print("Lista de tarefas:")
        for tarefa in tarefas:
            print("-", tarefa)
    else:
        print("Opção inválida. Tente novamente.")
