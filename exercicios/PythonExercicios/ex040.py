n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f} '.format(n1, n2, m))
if m >= 7 :
    print('\033[32m PARABÉNS VOCÊ ESTA APROVADO! \033[m')
elif m >= 5 and m <= 6.9 :
    print('\033[34m O aluno está de RECUPERAÇÃO! \033[m ')
else:
    print('\033[31m O aluno está de REPROVADO! \033[m ')
