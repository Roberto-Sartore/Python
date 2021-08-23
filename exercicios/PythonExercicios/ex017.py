from math import hypot
'''co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
print('A hipotenusa dos catetos é {:.2f}'.format((co ** 2 + ca ** 2) ** (1 / 2)))'''

co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
print('A hipotenusa dos catetos é {:.2f}'.format(hypot(co,ca)))