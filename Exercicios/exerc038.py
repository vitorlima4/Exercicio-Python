# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1 > numero2:
    print('O primeiro número {} é maior do que o segundo número {}.' .format(numero1, numero2))
elif numero2 > numero1:
    print('O segundo número {} é maior do que o primeiro número {}.' .format(numero2, numero1))
else:
    print('O primeiro número {} e o segundo número {}, são iguais.' .format(numero1, numero2))
