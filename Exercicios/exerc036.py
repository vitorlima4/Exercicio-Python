# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print('Você precisa de R${:.2f} para pagar uma casa no valor de R${:.2f} em {} anos.' .format(prestacao, casa, anos))

if prestacao <= minimo:
    print('O empréstimo bancário foi aprovado.')
else:
    print('O empréstimo bancário foi negado.')
