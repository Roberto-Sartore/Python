from time import sleep
n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número'))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('\033[33m Qual é a sua opção? \033[m'))
    if opcao == 1:
        soma = n1 + n2
        print('\033[34m A soma entre {} e {} é {} \033[m'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('\033[34m O produto de {} X {} é {} \033[m'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\033[34m Entre {} e {} o maior valor é {} \033[m'.format(n1, n2, maior))
    elif opcao == 4:
        print('\033[34m Informe os números novamente:\033[m')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opcao == 5:
        print('\033[32m Finalizando...\033[m')
    else:
        print('\033[31m Opção inválida. Tente novamente. \033[m')
    print('=-=' * 12)
    sleep(2)
print('\033[33m Fim do programa! Volte sempre! \033[m')




