"""Faça um Programa que leia três números e mostre o maior e o menor deles"""

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

maior = 0
menor = 0
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3


print(f'O maior valor digitado é {maior} e o menor é {menor}.')




# outra forma de fazer, mais simples.
lista = [n1, n2, n3]
print('O maior numero digitado foi: {} '.format(max(lista)))
print('O menor numero digitado foi: {} '.format(min(lista)))