# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

lista = list()
jogos = list()

print('--- Jogos da Mega Sena ---')

quantidade = int(input('Quantos jogos você quer que sorteie? '))
tot = 1
while tot <= quantidade:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('--- Números Sorteados ---')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
