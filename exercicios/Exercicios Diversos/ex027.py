"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
lista = [n1, n2, n3]
lista.sort(reverse=True)
print(f'Os números digitado em ordem descrescente são {lista}.')
