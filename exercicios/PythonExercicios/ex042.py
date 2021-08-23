print('ANALISADOR DE TRIANGULO.')
r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmento '))
r3 = float(input('Terceiro segmento '))
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