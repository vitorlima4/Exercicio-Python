# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para fazer a conversão:
[1] Converter para binário.
[2] Converter para octal.
[3] Converter para hexadecimal.''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O número {} convertido para binário fica {}.' .format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} convertido para octal fica {}.' .format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} convertido para hexadecimal fica {}.' .format(numero, hex(numero)[2:]))
else:
    print('Opção inválida.')
