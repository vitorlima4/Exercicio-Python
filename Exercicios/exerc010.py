# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1.00 = R$5.45

real = float(input('Quanto dinheiro você tem na carteira? '))

dolar = real / 5.45

print('Com R${:.2f}, você pode comprar US${:.2f}.' .format(real, dolar))
