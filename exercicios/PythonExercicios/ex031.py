dv = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {} Km.'.format(dv))
if dv <= 200:
    print('E o preço da sua passagem será R$ {:.2f}'.format(dv * 0.50))
else:
    print('E o preço da sua passagem será R$ {:.2f}'.format(dv * 0.45))

