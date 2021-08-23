while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 36)
    if num < 0 :
        break
    for c in range(1, 11):
        print(f'{num} X {c:2} = {num * c}')
    print('-' * 36)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')



