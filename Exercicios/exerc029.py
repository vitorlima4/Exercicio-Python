# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual a velocidade do seu carro? '))

if velocidade > 80:
    print('MULTADO! O limite permitido é de 80km/h')
    multa = (velocidade - 80) * 7
    print('O valor da multa é de R${:.2f}.' .format(multa))

print('Tenha um bom dia, dirija com segurança.')
