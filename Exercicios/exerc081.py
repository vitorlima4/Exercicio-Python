# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um número: ')))

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Lista: {lista}')

print(f'Foram digitados {len(lista)} números.')

lista.sort(reverse=True)
print(f'Lista decrescente {lista}')

if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')
