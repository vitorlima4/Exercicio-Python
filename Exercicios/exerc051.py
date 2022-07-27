# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

formula = primeiro + (10 - 1) * razao

for c in range(primeiro, formula + razao, razao):
    print('{}' .format(c), end=' > ')
print('Fim')