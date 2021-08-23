v = float(input('Qual é a velocidade atual do carro: '))
if v > 80:
    print('\033[31m MULTADO! Você excedeu o limite permitido que é de 80Km/h\033[m')
    print('Você deve pagar uma multa de R$ {:.2f}'.format((v - 80) * 7))

print('\033[32mTenha um bom dia! Dirija com segurança!\033[m ')