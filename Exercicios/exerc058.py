# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.

from random import randint

print('-=- Jogo da Adivinhação -=-')
print('--- Jogador x Computador ---')

computador = randint(0, 10)
jogador = int(input('Digite o número de 1 a 10: '))

tentativas = 0
while computador != jogador:
    jogador = int(input('Você não acertou, escolha um número de 1 a 10: '))
    tentativas += 1

print('Parabéns, você conseguiu acerta com {} tentativas.!' .format(tentativas))
