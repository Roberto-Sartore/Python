# ex11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
n1 = int(input('Digite o 1º numero inteiro: '))
n2 = int(input('Digite o 2º número inteiro: '))
n3 = float(input('digite o 3º número real: ').replace(',', '.'))
p = (n1 * 2) * (n2 / 2)
s = (n1 * 3) + n3
e = (n3 * n3 * n3)
print(f'O produto do dobro do primeiro com metade do segundo é {p} ')
print(f'A soma do triplo do primeiro com o terceiro é {s}.')
print(f'o terceiro elevado ao cubo é {e}.')
