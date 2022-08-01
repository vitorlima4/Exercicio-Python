# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
lista = []
maior = menor = 0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))

    if len(lista) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    lista.append(pessoas[:])
    pessoas.clear()

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]

    if resposta in 'N':
        break

print(f'Lista: {lista}')
print(f'Pessoas cadastradas: {len(lista)}.')
print(f'Maior peso: {maior}, Lista de pessoas pesadas: ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nMenor peso: {menor}, lista de pessoas leves: ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
