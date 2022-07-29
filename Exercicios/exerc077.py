# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('programar', 'aprender', 'java', 'python', 'computacao', 'praticar',
            'curso', 'estudar')
print(f'Palavras: {palavras}')
for p in palavras:
    print(f'\nNa palavre {p.upper()}, temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
