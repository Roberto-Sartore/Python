listagem = ('Lápis', 1.75, 'Borracha', 2, 'caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
print('=' * 48)
print(f'{"LISTAGEM DE PREÇOS":^48} ')
print('=' * 48)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<36}', end='')
    else:
        print(f'R$ {listagem[pos]:>9.2f} ')
print('=' * 48)

