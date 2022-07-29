# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
         'Dez', 'Onze', 'Doze', 'Treze', 'Catoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('Digite um número de 0 a 20: '))

    while numero > 20 or numero < 0:
        numero = int(input('Tente novamente, digite um número de 0 a 20: '))

    print(f'Você digitou o número {tupla[numero]}.')

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Você quer continuar? [S/N]')).strip().upper()[0]

    if resposta == 'N':
        break

