print('{:=^40}'.format(' LOJAS TEM DE TUDO '))
valor = float(input('Valor das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] até 2x no cartão
[ 4 ] 3xou mais no cartão''')
op = int(input('Qual opção de pagamento? '))
if op == 1:
    total = valor - (valor * 10 / 100)
elif op == 2:
    total = valor - (valor * 5 / 100)
elif op == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros'.format(parcela))
elif op == 4:
    total = valor + (valor * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros'.format(totparc, parcela))
else:
    total = valor
    print('\033[31m Opção de pagamento invalida! tente novamente \033[m')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(valor, total))


