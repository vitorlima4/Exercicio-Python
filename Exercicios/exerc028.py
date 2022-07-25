# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

computador = randint(0, 5)

print('--- Jogo da Adivinhação ---')
jogador = int(input('Qual número o computador escolheu de 0 a 5? '))

if computador == jogador:
    print('Parabéns você ganhou!! O computador escolheu  o número {}, que foi o mesmo que você digitou!' .format(computador))
else:
    print('Nao foi dessa vez... O computador escolheu o número {} e você escolheu o {}.' .format(computador, jogador))
