# DOCSTRINGS
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end= '')
        c += p
    print('FIM!')


# interactive help
help(contador)


print('='*36)


# PARAMETROS OPCIONAIS
def soma(a=0, b=0, c=0):
    print(f'A = {a},  B = {b} e C = {c} ')
    s = a + b + c
    print(f'A soma A + B + C = {s}')


soma(2, 5, 9)
soma(7, 5)
print('='*36)

# ESCOPO DE VARIAVEIS


def funcao():
    n1 = 5
    print(f'N1 dentro vale {n1} ')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')

print('='*36)

# RETORNO DE VALORES

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = soma(3, 2, 5)
r2 = soma(1, 7)
r3 =  soma(6)
print(f'Meus calculos deram {r1}, {r2} e {r3}. ')

