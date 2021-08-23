def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m ')
        else:
            valido = True
            return float(entrada)



def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31m ERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31m Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31m Usúario preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n

