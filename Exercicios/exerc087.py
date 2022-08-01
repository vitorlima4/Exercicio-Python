# Aprimore o desafio 86, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaColuna = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha}, {coluna}:'))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
    print()

print(f'A soma dos valores pares: {somaPar}.')

for linha in range(0, 3):
    somaColuna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna: {somaColuna}')

for coluna in range(0, 3):
    if coluna == 0 or matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'Maior valor da segunda linha: {maior}')
