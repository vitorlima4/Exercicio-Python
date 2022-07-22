# Crie um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo
# e todas as informações possíveis sobre ele.

valor = input('Escreva algo: ')

print("O tipo primitivo desse valor é: ", type(valor))
print('Tem espaços? ', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabético? ', valor.isalpha())
print('É alfanumérico? ', valor.isalnum())
print('Está em maiúscula? ', valor.isupper())
print('Está em minúscula? ', valor.islower())
print('É capitalizada? ', valor.istitle())
