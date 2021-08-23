def titulo(txt):
    print('-'*36)
    print(txt)
    print('-'*36)


titulo('Curso em video')
titulo('AprendaPython')


print('#'*40)
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(b=4, a=5)
soma(7, 2)


print('#'*40)
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s} ')


soma(5, 2)
soma(2, 9, 4)


print('#'*40)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)


