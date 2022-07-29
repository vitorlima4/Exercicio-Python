# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

nAleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Números gerados: {nAleatorios}')
print(f'O maior valor gerado foi: {max(nAleatorios)}.')
print(f'O menor valor gerado foi: {min(nAleatorios)}.')
