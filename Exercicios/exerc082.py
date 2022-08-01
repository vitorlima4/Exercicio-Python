# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.


lista = []
pares = []
impares = []

while True:
    numeros = (int(input('Digite um número: ')))
    lista.append(numeros)

    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Lista: {lista}')
print(f'Lista com números pares: {pares}')
print(f'Lista com números ímpares: {impares}')
