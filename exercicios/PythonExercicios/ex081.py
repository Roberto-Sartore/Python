lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    cont += 1
    if resp in 'Nn':
        break
print('=' * 48)
print(f'Você digitou {len(lista)} elementos ')
lista.sort(reverse = True)
print(f'A lista de valores, ordenada de forma descrecente é {lista} ')
if 5 in lista:
    print('O valor 5 faz parte da lista! ')
else:
    print('O valor 5 Não foi encotrado na lista!.')
