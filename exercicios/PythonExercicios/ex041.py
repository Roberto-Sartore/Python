from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade <= 9 :
    print('O atleta tem {} anos em {} e sua categoria é \033[34m MIRIM \033[m'.format(idade, atual))
elif idade <= 14 :
    print('O atleta tem {} anos em {} e sua categoria é \033[34m INFANTIL \033[m'.format(idade, atual))
elif idade <= 19 :
    print('O atleta tem {} anos em {} e sua categoria é \033[34m JÚNIOR \033[m'.format(idade, atual))
elif idade <= 25 :
    print('O atleta tem {} anos em {} e sua categoria é \033[34m SÊNIOR \033[m'.format(idade, atual))
else:
    print('O atleta tem {} anos em {} e sua categoria é \033[34m MASTER \033[m'.format(idade, atual))
