# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0
while True:
    computador = randint(0, 100)
    jogador = int(input('Escolha um número: '))

    parImpar = ' '
    while parImpar not in 'PI':
        parImpar = str(input('Você quer par ou ímpar [P/I]? ')).strip().upper()[0]

    soma = computador + jogador

    print(f'Computador escolheu {computador} e o jogador escolheu {jogador}, a soma dos números deu {soma}.')
    if soma % 2 == 0:
        print('A soma dos números deu par.')
        if parImpar == 'P':
            print('Jogador venceu!')
            vitorias += 1
        else:
            print('Computador venceu!')
            break
    else:
        print('A soma dos números deu ímpar.')
        if parImpar == 'I':
            print('Jogador venceu!')
            vitorias += 1
        else:
            print('Computador venceu!')
            break

print(f'O jogador conseguiu {vitorias} vitórias consecutivas.')


