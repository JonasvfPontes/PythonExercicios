matriz = [[[], [], []], [[], [], []], [[], [], []]]
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f'Digite um valor para [{i}] [{c}] '))
print(f'\33[4:34m{"Matriz Gerada":^30}\33[m')
somaPares = soma3coluna = 0
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]}] ', end='')
        if matriz[i][c] % 2 == 0: #Somar se o valor for PAR
            somaPares += matriz[i][c]
        if c == 2:
            soma3coluna += matriz[i][c]
    print('')
print(f'\n\33[4:32m{"Resultados:"}\33[m')
print(f'A) soma de todos os números pares: {somaPares}')
print(f'B) Soma da 3ª coluna é: {soma3coluna}')
print(f'C) O maior valor da 2ª linha é: {max(matriz[1])}')
