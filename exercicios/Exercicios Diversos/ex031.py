"""Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
 se digitar outro valor deve aparecer valor inválido"""
print('Digite um numero para o dia da semana, sendo')
print('1 Domingo')
print('2 Segunda feira')
print('3 Terça feira')
print('4 Quarta feira')
print('5 Quinta feira')
print('6 Sexta feira')
print('7 Sabado')
num = int(input('Qual sua opção: '))
if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda feira')
elif num == 3:
    print('Terça feira')
elif num == 4:
    print('Quarta feira')
elif num == 5:
    print('Quinta feira')
elif num == 6:
    print('Sexta feira')
elif num == 7:
    print('Sabado')
else:
    print('Opção Inválida!')
