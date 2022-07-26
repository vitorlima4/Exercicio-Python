# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

lado1 = float(input('Informe o primeiro lado: '))
lado2 = float(input('Informe o segundo lado: '))
lado3 = float(input('Informe o terceiro lado: '))


if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Podem forma um triângulo.')
    if lado1 == lado2 == lado3:
        print('Triângulo equilátero.')
    elif lado1 != lado2 != lado3 != lado1:
        print('Triângulo escaleno.')
    else:
        print('Triângulo isósceles.')
else:
    print('Não podem forma um triângulo')
