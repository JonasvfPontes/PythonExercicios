todos = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}º valor: '))
    if num % 2 == 0:
        todos[0].append(num)
    else:
        todos[1].append(num)
print('_' * 30)
todos[0].sort()
todos[1].sort()
print(f'Os valores PARES são {todos[0]}')
print(f'Os valores IMPARES são {todos[1]}')


