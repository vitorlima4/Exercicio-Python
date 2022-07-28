# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = 'S'
media = soma = cont = maior = menor = 0

while continuar == 'S':
    numero = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media = soma / cont
print('Média: {}.' .format(media))
print('Maior {} e Menor {}.' .format(maior, menor))
