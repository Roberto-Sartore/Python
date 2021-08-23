nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Muito prazer em te conhecer!')

# retorna o primeiro nome.
print('Seu primeiro nome é {}'.format(n[0]))

# Retorna o ultimo nome.
print('Seu último nome é {}'.format(n[len(n)-1]))

