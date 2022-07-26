# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Qual seu ano de nascimento? '))

anoAtual = date.today().year
idade = anoAtual - ano

print('Você nasceu no ano de {}, sua idade é de {} anos em {}.' .format(ano, idade, anoAtual))

if idade < 18:
    print('Ainda faltam {} anos para o alistamento.' .format(18 - idade))
    print('Seu alistamento será em {}.'.format(ano + 18))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.' .format(idade - 18))
    print('Seu alistamento foi em {}.'.format(ano + 18))
else:
    print('Você tem que se alistar imediatamente!')

