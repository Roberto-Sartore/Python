# ex 13
#Tendo como entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

alt = float(input('Qual sua altura? ').replace(',', '.'))
sexo = str(input('Qual seu sexo? [M/F]: ').upper())
if sexo == 'M':
    p = (72.7 * alt) - 58
    print(f'Seu peso ideal é {p:.2f}')
elif sexo == 'F':
    p = (62.1 * alt) - 44.7
    print(f'Seu peso ideal é {p:.2f}')
else:
    print('Sexo inválido')
