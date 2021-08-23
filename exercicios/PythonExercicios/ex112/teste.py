from utilidadescev import moeda
from utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 35, 22)
n1 = dado.leiaInt('Digite um Inteiro: ')
n2 = dado.leiaFloat('Digite um Real: ')
print(f'O valor Inteiro digitado foi {n1} e o Real foi {n2}')