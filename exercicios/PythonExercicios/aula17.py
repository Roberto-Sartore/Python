num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
print(num)
print(f'Essa lista tem {len(num)} elementos. ')
print('='*36)



valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('='*36)


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('='*36)


a = [2, 3, 4, 7]
b = a # liga uma lista a outra, o que eu alterar em uma alera tambem na outra.
b = a[:] # copia a lista a para b, mas elas continuam independentes.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista A: {b}')
print('='*36)



