"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento"""

salario = float(input('Qual o salário do coloborador R$: '))
if salario <= 280.00:
    aumento = salario + ((salario/100) * 20)
    print(f'Salario atual R$ {salario}, percentual de aumento 20% no valor de R$ {((salario/100) * 20)}, o novo Salario sera R$ {aumento}.')
elif salario > 280.00 and salario <= 700.00:
    aumento = salario + ((salario / 100) * 15)
    print(f'Salario atual R$ {salario}, percentual de aumento 15% no valor de R$ {((salario / 100) * 15)}, o novo Salario sera R$ {aumento}.')
elif salario > 700.00 and salario <= 1500.00:
    aumento = salario + ((salario / 100) * 10)
    print(f'Salario atual R$ {salario}, percentual de aumento 10% no valor de R$ {((salario / 100) * 10)}, o novo Salario sera R$ {aumento}.')
elif salario > 1500.00:
    aumento = salario + ((salario / 100) * 5)
    print(f'Salario atual R$ {salario}, percentual de aumento 5% no valor de R$ {((salario / 100) * 5)}, o novo Salario sera R$ {aumento}.')
