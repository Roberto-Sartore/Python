# ex 15
"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e
mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a)salário bruto.
b)quanto pagou ao INSS.
c)quanto pagou ao sindicato.
d)o salário líquido.
e)calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido"""

vh = float(input('Quanto você ganha por hora R$: ').replace(',', '.'))
h = float(input('Quantas horas você trabalhou no mês: ').replace(',', '.'))
sb = h * vh
ir = (sb/100)*11
inss = (sb/100)*8
sind = (sb/100)*5
sl = sb - ir - inss - sind
print(f'Com {h:.2f} horas trabalhadas a R$: {vh:.2f} por hora, seu sálario Bruto é R$: {sb:.2f} no mês. ')
print(f'Desconto de INSS no valor de R$ {inss:.2f}')
print(f'O valor pago ao sindicato é R$ {sind:.2f}')
print(f'O salário liquido é R$ {sl:.2f}')
