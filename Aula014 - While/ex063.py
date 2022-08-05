print('SEQUÊNCIA FIBONACCI')
n = int(input('Digite um número inteiro: '))
a = 0
b = 1
c = 0
cont = 2
print(f'{a}, {b}', end='')
while cont < n:
    c = a + b
    print(f', {c}', end='')
    a = b
    b = c
    cont += 1
print('.')
