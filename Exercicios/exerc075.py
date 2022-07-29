# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = (int(input('Digite o primerio valor: ')),
        int(input('Digite o segundo valor: ')),
        int(input('Digite o terceiro valor: ')),
        int(input('Digite o quarto valor: ')))

print(f'Valores cadastrados: {valores}')
print(f'Quantas vezes apareceu o valor 9? {valores.count(9)} vezes.')

if 3 in valores:
    print(f'Em que posição foi digitado o primeiro valor 3? {valores.index(3) + 1}º posição.')
else:
    print('O valor 3 não foi digitado.')
print('Quais foram os números pares? ', end='')
for par in valores:
    if par % 2 == 0:
        print(par, end=' ')
