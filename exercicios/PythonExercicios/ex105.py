def notas(*n, sit=False):
    """
    -> Função para analizar notas e situação de varios alunos.
    :param n: uma ou mais notas dos alunos(aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionario com varias informações sobre a situação da turma.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 8.5, 9.5, 8, sit=True)
print(resp)
print('='*36)
help(notas)
