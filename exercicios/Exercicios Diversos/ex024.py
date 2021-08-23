"""Faça um Programa que leia três números e mostre o maior deles."""
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior valor digitado!')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior valor digitado!')
elif n3 > n1 and n3 > n2:
    print(f'{n3} é o maior valor digitado!')
else:
    print(f'{n1}, {n2} e {n3} são iguais!')