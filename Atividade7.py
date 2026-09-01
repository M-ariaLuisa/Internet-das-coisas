#Gere um número aleatório entre 1 e 20.
#  Em um while True , peça palpites até que o usuárioacerte.
# Informe se cada palpite foi maior ou menor que o número sorteado, conte as tentativas e
#encerre com break quando houver acerto.


import random

numero = random.randint(1, 20)
tentativas = 0

while True:
    palpite = int(input("Digite seu palpite (1 a 20): "))
    tentativas += 1

    if palpite > numero:
        print("O palpite é maior que o número sorteado.")
    elif palpite < numero:
        print("O palpite é menor que o número sorteado.")
    else:
        print("Parabéns! Você acertou!")
        print(f"Você precisou de {tentativas} tentativa(s).")
        break