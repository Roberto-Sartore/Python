from random import randint
from time import sleep
comp = randint(0, 5) #Faz o computador escolher um numero aleatorio entre 0 e 5.
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jog = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(2)
if jog == comp:
    print('Parabéns você conseguiu me vencer! ')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(comp, jog))

