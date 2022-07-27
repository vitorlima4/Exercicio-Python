# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaIdd = 0
homemVelho = 0
nomeHomem = ''
mulherNova = 0

for c in range(1, 5):
    nome = str(input('Qual o nome da {}º pessoa? ' .format(c))).strip()
    idade = int(input('Qual a idade da {}º pessoa? ' .format(c)))
    sexo = str(input('Qual o sexo da {}º pessoa? [M/F]' .format(c))).strip().upper()

    # Somando a idade do grupo
    somaIdd += idade

    # Verificando homem
    if c == 1 and sexo in 'M':
        homemVelho = idade
        nomeHomem = nome
    if sexo in 'M' and idade > homemVelho:
        homemVelho = idade
        nomeHomem = nome

    # Verificando mulher
    if sexo in 'F' and idade < 20:
        mulherNova += 1

media = somaIdd / 4
print('A média da idade do grupo é de {}.' .format(media))
print('O nome do homem mais velho é {} e ele tem {} anos.' .format(nomeHomem, homemVelho))
print('Tem {} mulheres menores de 20 anos.' .format(mulherNova))
