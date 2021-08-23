a = float(input('qual a altura da sua parede? '))
l = float(input('qual a largura da sua parede? '))
print('A dimensão é {} x {} e sua area é {:.2f} m².'.format(a, l, (a*l)))
print('Para pintar essa parede sera necessario {:.1f}l de tinta'.format((a*l)/2))
