# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em
# uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]

for c in range(0, 7):
    valores = int(input('Digite um número: '))

    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)
numeros[0].sort()
numeros[1].sort()
print(f'Pares: {numeros[0]}')
print(f'ímpares: {numeros[1]}')
