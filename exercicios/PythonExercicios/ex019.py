import random
p = input('Primeiro aluno: ')
s = input('Segundo aluno:')
t = input('Terceiro aluno:')
q = input('Quato aluno:')
lista = [p, s, t, q]
esc = random.choice(lista)
print('O aluno escolhido foi {}'.format(esc))
