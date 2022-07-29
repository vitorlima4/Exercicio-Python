# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Lápis', 1.75,
         'Borracha', 3.50,
         'Caneta', 2,
         'Estojo', 7.55,
         'Caderno', 25,
         'Mochila', 120)

print(f'{"Listagem de Preços":^40}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
