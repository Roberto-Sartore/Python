from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
print('''Qual seu sexo?
[ 1 ] Masculino
[ 2 ] Feminino''')
sexo = int(input('Sua opçao: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18 and sexo == 1:
    print('Você tem que se alistar \033[32m IMEDIATAMENTE! \033[m')
elif idade < 18  and sexo == 1:
    print('Ainda faltam \033[33m {} anos \033[m para o alistamento '.format(18 - idade))
    print('Seu alistamento será \033[33m {} \033[m.'.format(atual + (18 - idade)))
elif idade > 18 and sexo == 1 :
    print('Você deveria ter se alistado há \033[31m {} anos. \033[m '.format(idade - 18))
    print('Seu alistamento foi em \033[31m {} \033[m.'.format(atual - (idade - 18)))
elif sexo != 1 and sexo != 2 :
    print('Opção inválida! tente novamente.')
else:
    print('No Brasil o serviço militar não é obrigatório ao sexo Feminino!')
