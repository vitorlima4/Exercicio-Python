# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

numero = float(input('Digite um número real: '))
print('A porção inteira do valor digitado é {}.' .format(math.trunc(numero)))
