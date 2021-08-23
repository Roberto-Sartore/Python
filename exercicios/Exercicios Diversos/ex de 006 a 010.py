# exercicio 6 pedir o raio e calculara a area

r = float(input('Qual o raio do circulo em metros: ').replace(',', '.'))
a = 3.14 * (r * r)
print(f'Um circulo com raio {r} m possui area de {a} m².')
print('-' * 36)

# exercicio 7 calcular a area do quadrado mostrar a area e o dobro da area

l = float(input('Qual a largura em metros: ').replace(',', '.'))
c = float(input('Qual o comprimento em metros: ').replace(',', '.'))
a = l * c
d = a * 2
print(f'A area do quadrado é {a:.2f} m² e o dobro da area é {d:.2f} m²')
print('-' * 36)

# exercicio 8 calcular salario mensal recebendo valor por hora e horas trabalhadas

vh = float(input('Quanto você ganha por hora R$: ').replace(',', '.'))
h = float(input('Quantas horas você trabalhou no mês: ').replace(',', '.'))
s = h * vh
print(f'Com {h:.2f} horas trabalhadas a R$: {vh:.2f} por hora, seu sálario sera de R$: {s:.2f} no mês. ')
print('-' * 36)

# exercicio 9 receber fahrenheit e converter para celsius

gf = float(input('Qual a temperatura em Fahrenheit: ').replace(',', '.'))
gc = (gf - 32)/1.8
print(f'A temperatura {gf:.2f} Fahrenheit é igual {gc:.2f} Celsius ')
print('-'*36)

# exercicio 10 receber celsius e converter para fahrenheit

gc = float(input('Qual a temperatura em Celsius: ').replace(',', '.'))
gf = gc*1.8+32
print(f'A temperatura {gc:.2f} Celsius é igual {gf:.2f} Fahrenheit ')
print('-'*36)

