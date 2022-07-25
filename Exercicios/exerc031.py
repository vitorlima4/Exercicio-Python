# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da viagem em KM? '))

print('Você está prestes a começar uma viagem de {:.1f}km.' .format(distancia))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print('E o preço da passagem será de R${:.2f}.' .format(passagem))
