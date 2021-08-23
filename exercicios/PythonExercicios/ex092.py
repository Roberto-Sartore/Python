from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['Ctps'] = int(input('Carteira de Trabalho (0 não tem) : '))
if dados['Ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=' * 36)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v} ')


