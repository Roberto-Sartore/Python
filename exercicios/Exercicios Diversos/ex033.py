"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem
ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""

r1 = int(input('Digite o tamanho do 1º lado: '))
r2 = int(input('Digite o tamanho do 2º lado: '))
r3 = int(input('Digite o tamanho do 3º lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[32m PODEM FORMAR \033[m um triângulo! ', end='')
    if r1 == r2 == r3:
        print('\033[34m EQUILÁTERO! \033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[34m ESCALENO! \033[m')
    else:
        print('\033[34m ISÓCELES! \033[m')
else:
    print('Os segmentos acima \033[31m NÃO PODEM FORMAR \033[m triângulo! ')