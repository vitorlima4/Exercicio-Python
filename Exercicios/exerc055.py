# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Informe o peso da {}º pessoa: ' .format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('De 5 pessoas, o maior peso foi de {}kg e o menor peso foi de {}kg.' .format(maior, menor))

