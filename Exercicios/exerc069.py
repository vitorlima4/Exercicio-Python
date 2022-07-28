# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

pMaiores = sexoM = sexoF = 0

while True:
    print('### CADASTRE PESSOAS ###')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    if idade >= 18:
        pMaiores += 1

    if sexo == 'M':
        sexoM += 1

    if sexo == 'F' and idade < 20:
        sexoF += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar cadastrando? [S/N]')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Tem {pMaiores} pessoas com mais de 18 anos.')
print(f'Homens cadastrados: {sexoM}.')
print(f'Tem {sexoF} mulheres com menos de 20 anos.')
