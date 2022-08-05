print('Vamos calcular o fatorial de um número')
n = int(input('Digite o número '))
inicio = n
total = n * (n-1)
n -= 1
while n != 1:
    total *= (n - 1)
    n -= 1
print(f'{inicio}! é {total}')

