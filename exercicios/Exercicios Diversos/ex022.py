"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante"""

l = str(input('Digite uma letra: ').upper().strip())
if l in 'AEIOU':
    print(f'A letra {l} é uma vogal.')
else:
    print(f'{l} não é vogal')
