nome = str(input('Qual é seu nome? ')).upper()
if nome == 'ROBERTO' or nome == 'OBA':
    print('Que nome bonito!')
elif nome == 'PEDRO' or nome =='JOSE' or nome == 'JOAO' or nome == 'MARIA':
    print('Seu nome é bem popular no Brasil. !')
elif nome in ' THAIS LORENA':
    print('Belo nome feminino!')
else:
    print('Que nome comum você tem!')
print('Tenha um bom dia, {} !'.format(nome))
