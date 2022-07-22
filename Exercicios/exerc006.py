# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print('Dobro: {} \nTriplo: {} \nRaiz quadrada: {:.2f}' .format(dobro, triplo, raiz))
