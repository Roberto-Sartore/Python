from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor:'))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end = '')
    print('\033[33m DEU PAR\033[m' if total % 2 == 0 else '\033[33m DEU IMPAR \033[m')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[32m Você VENCEU! \033[m')
            v += 1
        else:
            print('\033[31m Você PERDEU! \033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[32m Você VENCEU! \033[m')
            v += 1
        else:
            print('\033[31m Você PERDEU! \033[m')
            break
    print('Vamos jogar novamente... ')
print(f'GAME OVER! Você venceu {v} vezes.')

