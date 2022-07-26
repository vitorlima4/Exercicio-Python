# Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

valor = float(input('Preço das compras: R$'))

print('''
FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    valorFinal = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.' .format(valorFinal))
elif opcao == 4:
    parcela = int(input('Quantas parcela deseja pagar? '))
    total = valor + (valor * 20 / 100)
    valorFinal = total / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(parcela, valorFinal))
else:
    print('Opção inválida, tente novamente.')

print('Sua compra no valor de R${:.2f}, vai custa R${:.2f} no final.' .format(valor, total))

