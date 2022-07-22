# Escreva um programa que leia um valor em metros e o exiba convertido.

metros = float(input('Digite a distância em metros: '))

km = metros / 10 ** 3
hm = metros / 10 ** 2
dam = metros / 10
dm = metros * 10
cm = metros * 10 ** 2
mm = metros * 10 ** 3

print('A medida de {}m corresponde a: ' .format(metros))
print('Km: {} \nHm: {} \nDam: {} \nDm: {} \nCm: {} \nMm: {}' .format(km, hm, dam, dm, cm, mm))
