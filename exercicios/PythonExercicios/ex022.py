nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

#transformar o nome em caixa alta.
print('Seu nome em maiúsculas é {}'.format(nome.upper()))

#transformar o nome em caixa baixa.
print('Seu nome em minúsculas é {}'.format(nome.lower()))

# contar quantas letras tem ao todo no nome sem os espaços
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

# contar quantas letras tem o primeiro nome (primeira opção)
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

# contar quantas letras tem o primeiro nome (segunda opção)
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

