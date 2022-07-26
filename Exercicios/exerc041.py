# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

nascimento = int(input('Informe seu ano de nascimento: '))

idade = date.today().year - nascimento

print('O atleta tem {} anos.' .format(idade))
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Júnior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')

