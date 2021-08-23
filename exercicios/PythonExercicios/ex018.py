import math
a = float(input('Digite o angulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O ângulo de {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(a, s, c, t))

