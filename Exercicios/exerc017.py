# Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot

oposto = float(input('Informe o cateto oposto: '))
adjacente = float(input('Informe o cateto adjacente: '))

# hipotusa^2 = oposto^2 + adjacente^2
hipotenusa = hypot(oposto, adjacente)

print('A hipotenusa vai medir: {:.2f}.'.format(hipotenusa))
