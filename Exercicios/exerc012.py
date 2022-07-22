# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual é o preço do produto? R$'))

valor = preco - (preco * 5 / 100)

print('O produto com desconto de 5% está custando R${:.2f}.' .format(valor))