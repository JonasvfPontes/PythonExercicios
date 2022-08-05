matriz = [[[], [], []], [[], [], []], [[], [], []]]
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f'Digite um valor para [{i}] [{c}] '))
print('_' * 30)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]}] ', end='')
    print('')

