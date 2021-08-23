from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[1:33m JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\033[m')
print('-=' * 12)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if comp == 0:
    if jogador == 0:
        print('\033[33m EMPATE \033[m')
    elif jogador == 1:
        print('\033[32m JOGADOR VENCE \033[m')
    elif jogador == 2:
        print('\033[34m COMPUTADOR VENCE \033[m')
    else:
        print('\033[31m JOGADA INVÁLIDA! \033[m')

elif comp == 1:
    if jogador == 0:
        print('\033[34m COMPUTADOR VENCE \033[m')
    elif jogador == 1:
        print('\033[33m EMPATE \033[m')
    elif jogador == 2:
        print('\033[32m JOGADOR VENCE \033[m')
    else:
        print('\033[31m JOGADA INVÁLIDA! \033[m')


elif comp == 2:
    if jogador == 0:
        print('\033[32m JOGADOR VENCE \033[m')
    elif jogador == 1:
        print('\033[34m COMPUTADOR VENCE \033[m')
    elif jogador == 2:
        print('\033[33m EMPATE \033[m')
    else:
        print('\033[31m JOGADA INVÁLIDA! \033[m')



