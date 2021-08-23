times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitoria', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('=' * 36)
print(f'Lista de times: {times} ')
print('=' * 36)
print(f'Os 5 primeiros são {times[0:5]}')
print('=' * 36)
print(f'Os 4 últimos são {times[-4:]}')
print('=' * 36)
print(f'Times em ordem Alfabetica: {sorted(times)}')
print('=' * 36)
print(f'O Corinthians está na {times.index("Corinthians")+1} ª posição.')
