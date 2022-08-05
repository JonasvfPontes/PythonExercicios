from random import randint
num = (randint(0,10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
menor = 0
maior = 0
print(num)
for c in range(0, 5):
    if c == 0:
        menor = num[c]
        maior = num[c]
    else:
        if num[c] < menor:
            menor = num[c]
        if num[c] > maior:
            maior = num[c]
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
# Outra forma de encontrar o máximo e o mínino é:
print(f'\n\33[36mO maior valor é {max(num)}')
print(f'O menor valor é {min(num)}')
