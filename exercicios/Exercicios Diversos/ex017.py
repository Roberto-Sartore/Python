# ex17
"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias"""
import math
area = float(input('Qual a area a ser pintada em m²: ').replace(',', '.'))
print("1) Calcular a área a ser pintada")
print("2) Preços dos produtos")
print("3) Calcular os preços por área a ser pintada")
print("4) Sair do programa")

litros = float(area / 6)
litrosf = math.ceil(float(litros*1.0))
latas = math.ceil(float(litrosf) / 18)
galoes = math.ceil(float(litrosf) / float(3.6))
preco  = latas * 80
precogaloes = galoes*25.0
while True:
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        l = float(input('Qual a largura em metros: ').replace(',', '.'))
        c = float(input('Qual o comprimento em metros: ').replace(',', '.'))
        a = l * c
        print(f'A area a ser pintada é {a:.2f} m².')
    elif opcao == 2:
        print('Galão de 3,6L', '-'*10, 'R$ 25,00')
        print('Lata de 18L', '-'*12, 'R$ 80,00')
    elif opcao == 3:
        a1 = int(litrosf / 18)
        a2 = litrosf % 18
        a3 = math.ceil(a2 / 3.6)
        a4 = ((a1 * 80) + (a3 * 25))
        while True:
            print('Para comprar apenas latas de 18 litros digite 1')
            print('Para comprar apenas galões de 3,6 litros digite 2')
            print('Para misturar latas e galões digite 3')
            print('Para SAIR Digite 4')
            op = int(input('Digite sua opção: '))
            if op == 1:
                print(f'Para pintar a area de {area:.2f} m² serão necessarios {latas:.2f} latas por demão no valor de R$ {preco:.2f}.')
            elif op == 2:
                print(f'Para pintar a area de {area:.2f} m² serão necessarios {galoes:.2f} Galoes por demão no valor de R$ {precogaloes:.2f}.')

            elif op == 3:
                print(
                    f'Para pintar a area de {area:.2f} m² serão necessarios {a1} latas, {a3} galoes por demão no valor de R$ {a4:.2f}.')
            elif op == 4:
                print('Até logo!')
                break
            else:
                print('Opção invalida!')
            print('=' * 48)

    else:
        print('Opção invalida!')
    break
print()



