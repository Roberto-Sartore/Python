n = 0
cont = 0
total = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont += 1
    total += n
    n = int(input('Digite um número [999 para parar]: '))
    if cont == 1:
        num = 'número'
    else:
        num = 'números'
print('Você digitou {} {}  e a soma entre eles foi {}!'.format(cont,num, total))

