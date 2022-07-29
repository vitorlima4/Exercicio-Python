# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
# valores únicos digitados, em ordem crescente.

valoresNum = []
cadastrar = int(input('Quantos números você quer cadastrar? '))

for c in range(0, cadastrar):
    valor = int(input('Digite um número inteiro: '))

    if valor not in valoresNum:
        valoresNum.append(valor)
        print('Número cadastrado.')
    else:
        print('Número já cadastrado na lista, não adicionarei. ')

valoresNum.sort()
print(f'Os valores cadastrados em ordem crescente: {valoresNum}')
