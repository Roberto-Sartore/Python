sal = float(input('Qual é o salario do funcionario? R$ '))
if sal > 1250:
    alm = sal + (sal * 10 / 100)
if sal <= 1250:
    alm = sal + (sal * 15 /100)
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(sal, alm))
