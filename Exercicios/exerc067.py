# Faça um programa que mostre a tabuada de vários números, um de cada vez,  para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Digite um número (Número negativo interrompe o programa): '))

    if numero < 0:
        break

    for c in range(1, 11):
        mult = numero * c
        print(f'{numero} * {c} = {mult}')

print('Programa de tabuada finalizado.')
