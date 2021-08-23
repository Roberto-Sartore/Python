"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo"""
n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'{n} é um número PAR.')
else:
    print(f'{n} é um número IMPAR.')
