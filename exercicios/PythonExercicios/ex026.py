frase = str(input('Digite uma frase: ')).upper().strip()
# conta quantas vezes aparece a letra a na frase.
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))

# mostra em que posição aparece a letra A pela primeira vez.
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))

# mostra em que posição aparece a ultima letra A.
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))
