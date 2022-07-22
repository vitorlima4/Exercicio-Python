# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe seu salário: R$'))

novo = salario + (salario * 15 / 100)

print('Seu salário agora com aumento de 15%, passou para R${:.2f}.' .format(novo))