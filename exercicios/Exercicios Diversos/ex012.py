# ex12 Tendo como entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# fórmula: (72.7*altura) - 58

alt = float(input('Qual sua altura? ').replace(',', '.'))
p = (72.7 * alt) - 58
print(f'Seu peso ideal é {p:.2f}')
