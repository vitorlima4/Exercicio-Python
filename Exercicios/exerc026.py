# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase: ')).lower().strip()

print('A letra A aparece {} na frase.' .format(frase.count('a')))
print('A primeira letra A se encontra na posição {}.' .format(frase.find('a') + 1))
print('A última letra A se encontra na posição {}.' .format(frase.rfind('a') + 1))
