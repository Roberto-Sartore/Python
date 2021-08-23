n = int(input('Digite um numero qualquer:'))
if n % 2 == 0:
    print('O número {} é \033[32m Par!\033[m'.format(n))
else:
    print('O número {} é \033[31m Impar!\033[m'.format(n))
