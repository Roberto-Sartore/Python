num = [[], []]
valor = 0
for C in range (1, 8):
    valor = int(input(f'Digite o {C}º. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=' * 48)
num[0].sort()
num[1].sort()
print(f'Os Valores pares digitados foram: {num[0]}')
print(f'Os Valores impares digitados foram: {num[1]}')

