# exercicio 1 Ola mundo
print('Olá Mundo!')
print('-' * 36)

# EXERCICIO 2 mostrar numero informado

n = int(input('informe um número: '))
print(f'O valor informado foi {n}')
print('-' * 36)

#exercicio 3 pedir 2 numeros e mostrar a soma

n1 = int(input('informe o 1º número: '))
n2 = int(input('informe o 2º número: '))
s = n1 + n2
print(f'A soma de {n1} + {n2} é {s}')
print('-' * 36)

#exercicio 4 pedir 4 notas e mostrar a média

n1 = float(input('informe a 1º nota: ').replace(',', '.'))
n2 = float(input('informe a 2º nota: ').replace(',', '.'))
n3 = float(input('informe o 3º nota: ').replace(',', '.'))
n4 = float(input('informe o 4º nota: ').replace(',', '.'))
m = (n1+n2+n3+n4)/4
print(f'A media é {m:.2f}.')
print('-' * 36)

#exrcicio 5 converter metros para centimetro

m = float(input('Informe a medida em metros: ').replace(',', '.'))
c = m * 100
print(f'{m} metros é igual a {c} centimetros.')



