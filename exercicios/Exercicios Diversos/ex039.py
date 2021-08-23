"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
 usuário, mostrando uma mensagem de erro e voltando a pedir as informações"""
nome = str(input('Login: ')).upper().strip()
senha = str(input('Senha: ')).upper().strip()
while nome == senha:
    print('Sua Senha deve ser diferente do Login')
    senha = str(input('Senha: ')).upper().strip()
print('Cadastro Aprovado!')