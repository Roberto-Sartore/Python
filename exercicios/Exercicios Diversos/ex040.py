"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'"""


nome = str(input('Qual seu nome [minimo 4 caracteres]: ')).strip()
idade = int(input('Sua idade: ').strip())
sexo = str(input('Sexo [M/F]')).upper().strip()
salario = float(input('Salário R$: ').replace(',', '.').strip())
civil = str(input('Estado Civil [S/C/V/D]: ')).upper().strip()

while len(nome)<=3:
    nome = str(input('O nome deve ter mais de 3 caracteres: ')).strip()
while idade<0 or idade>150:
    idade = int(input('Sua idade: ').strip())
while sexo !='M' and sexo !='F':
    sexo = str(input('Sexo [M/F]')).upper().strip()
while salario < 0:
    salario = float(input('Salário R$: ').replace(',', '.').strip())
while civil !='S' and civil !='C' and civil !='V' and civil !='D':
    civil = str(input('Estado Civil [S/C/V/D]: ')).upper().strip()
