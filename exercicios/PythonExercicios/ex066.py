n = s = 0
cont = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Você digitou {cont} números e a soma vale {s}')