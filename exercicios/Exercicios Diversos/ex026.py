"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
 sabendo que a decisão é sempre pelo mais barato"""

p1 = float(input('Digite a 1º valor R$ : ').replace(',', '.'))
p2 = float(input('Digite a 2º valor R$ : ').replace(',', '.'))
p3 = float(input('Digite a 3º valor R$ : ').replace(',', '.'))
if p1 < p2 and p1 < p3:
    print ('O produto 1 é o mais barato!!')
elif p2 < p1 and p2 < p3:
    print ('O produto 2 é o mais barato!!')
elif p3 < p1 and p3 < p2:
    print ('O produto 3 é o mais barato!!')

    #Se alguns numeros forem iguais

elif p1 == p2 and p1 and p2 < p3:
    print ('O produto 1 e 2 são os mais baratos!!')
elif p1 == p3 and p1 and p3 < p2:
    print ('O produto 1 e 3 são os mais baratos!!')
elif p2 == p3 and p2 and p3 < p1:
    print ('O produto 2 e 3 são os mais baratos!!')

    #Se todo os numero forem iguais

else:
    print ('Todos os preços são iguais!!')
