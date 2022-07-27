# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(0, 6):
    numero = int(input('Escolha um número par: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('A soma entre os {} números pares foi de {}.' .format(cont, soma))
