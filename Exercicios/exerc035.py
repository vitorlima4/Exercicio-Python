# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

x = float(input('Primeiro segmento: '))
y = float(input('Segundo segmento: '))
z = float(input('Terceiro segmento: '))

if x + y > z and x + z > y and y + z > x:
    print('Podem forma um triângulo.')
else:
    print('Não podem forma um triângulo.')
