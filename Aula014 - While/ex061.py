print('='*5, 'PA', '='*5)
i = int(input('Digite um número '))
r = int(input('Qual a razão da PA '))
c = 0
while c < 10:
    print(i, end=' → ')
    i += r
    c += 1
print('Acabou')