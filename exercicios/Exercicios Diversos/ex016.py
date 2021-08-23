# ex16
"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
 pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
 latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
 preço total."""
import math
area = float(input('Qual a area a ser pintada em m²: ').replace(',', '.'))
litros = float(area / 3)
litrosf = math.ceil(float(litros*1.0))
latas = math.ceil(float(litrosf) / 18)
preco = latas * 80
print(f'Para pintar a area de {area:.2f} m² serão necessarios {latas:.2f} latas por demão no valor de R$ {preco:.2f}.')

