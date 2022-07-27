# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

opcao = 0
while opcao != 5:
    print('''---------------------------
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual sua opção de 1 a 5? '))

    if opcao == 1:
       soma =  valor1 + valor2
       print('A soma do {} + {} = {}.' .format(valor1, valor2, soma))
    elif opcao == 2:
        multiplicar = valor1 * valor2
        print('A multiplicação do {} * {} = {}.'.format(valor1, valor2, multiplicar))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('O maior valor é {}.' .format(maior))
    elif opcao == 4:
        valor1 = float(input('Digite o novo valor primeiro: '))
        valor2 = float(input('Digite o novo valor segundo: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente outro número de 1 a 5.')

print('Programa encerrado')

