# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))

total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print(c, end=' ')
        total += 1

print('\nO número {} foi divisível {} vezes.' .format(numero, total))

if total == 2:
    print('Número primo.')
else:
    print('Não é primo.')
