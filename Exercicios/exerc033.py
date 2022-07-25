# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

maior = numero1
if numero2>numero1 and numero2>numero3:
    maior = numero2
if numero3>numero1 and numero3>numero2:
    maior = numero3

menor = numero1
if numero2<numero1 and numero2<numero3:
    menor = numero2
if numero3<numero1 and numero3<numero2:
    menor = numero3

print('O maior número é {}.' .format(maior))
print('O menor número é o {}.' .format(menor))
