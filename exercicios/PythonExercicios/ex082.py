lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=' * 48)
print(f'A lista completa é {lista} ')
pares.sort()
print(f'A lista de pares é {pares} ')
impares.sort()
print(f'A lista dos impares é {impares} ')

