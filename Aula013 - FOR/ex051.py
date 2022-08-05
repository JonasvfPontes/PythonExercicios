print('='*5, 'PA', '='*5)
i = int(input('Digite um número '))
r = int(input('Qual a razão da PA '))
for c in range(0, 10):
    print(i, end=' → ')
    i += r
print('Acabou')