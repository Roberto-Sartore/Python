vc = float(input('Valor da casa: R$ '))
sc = float(input('Salário do comprador: R$ '))
tf = int(input('Quantos anos de financiamento'))
p = vc / (tf * 12)
min = sc * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação sera de R$ {:.2f}'.format(vc, tf, p))
if p <= min:
    print('Emprestimo pode ser CONCEDIDO! ')
else:
    print('Emprestimo NEGADO! ')
