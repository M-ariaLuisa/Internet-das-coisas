#Use a lista n u m e r o s = [ 1 2 , 7 , 9 , 2 0 , 3 1 , 4 4 , 1 8 , 5 ] .
#  Percorra os valores com for e conte quantos são pares e quantos são ímpares. Mostre as duas quantidades ao final.

numeros = [12, 7, 9, 20, 31, 44, 18, 5]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print("Quantidade de números pares:" , len(pares))
print("Quantidade de números impares:", len(impares))
