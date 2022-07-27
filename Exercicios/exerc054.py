# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input('Em que ano a {}º pessoa nasceu?: ' .format(c)))
    idade = date.today().year - nascimento
    if idade > 18:
        maior += 1
    else:
        menor += 1

print('De 7 pessoas, {} são maiores e {} são menores.' .format(maior, menor))
