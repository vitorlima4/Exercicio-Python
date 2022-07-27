# Faça um programa que leia um número qualquer e mostre o seu fatorial.

numero = int(input('Digite um número inteiro para calcular seu fatorial: '))

x = numero
fatorial = 1
while x > 0:
    print('{}' .format(x), end='')
    print(' x ' if x > 1 else ' = ', end='' )
    fatorial *= x
    x -= 1
print('{}.' .format(fatorial))




