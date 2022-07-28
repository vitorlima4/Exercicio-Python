# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

totGasto = pCaro = barato = cont = 0
nome = ''

while True:
    print('--- Loja Vitorino ---')
    produto = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço do produto? '))

    cont += 1
    totGasto += preco

    if preco >= 1000:
        pCaro += 1

    if cont == 1 or preco < barato:
        barato = preco
        nome = produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resposta == 'N':
        break

print('-'*20)
print(f'Total gasto: R${totGasto:.2f}')
print(f'Total de produtos que custam mais de R$1.000: {pCaro}')
print(f'O produto mais barato foi {nome} que custa R${barato:.2f}.')

