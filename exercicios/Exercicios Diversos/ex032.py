"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
 e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."""

n1 = float(input('Digite a 1º nota: ').replace(',', '.'))
n2 = float(input('Digite a 2º nota: ').replace(',', '.'))
media = (n1+n2)/2
if media >= 9 and media <= 10:
    print(f'Notas {n1} e {n2} com Média {media:.2f}')
    print('O aluno ficou com conceito A e esta APROVADO!')
elif media >= 7.50 and media < 9:
    print(f'Notas {n1} e {n2} com Média {media:.2f}')
    print('O aluno ficou com conceito B e esta APROVADO!')
elif media >= 6 and media < 7.50:
    print(f'Notas {n1} e {n2} com Média {media:.2f}')
    print('O aluno ficou com conceito C e esta APROVADO!')
elif media >= 4 and media < 6:
    print(f'Notas {n1} e {n2} com Média {media:.2f}')
    print('O aluno ficou com conceito D e esta REPROVADO!')
elif media >= 0 and media < 4:
    print(f'Notas {n1} e {n2} com Média {media:.2f}')
    print('O aluno ficou com conceito E e esta REPROVADO!')
