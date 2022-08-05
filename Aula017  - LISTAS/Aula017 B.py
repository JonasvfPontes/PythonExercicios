num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num, end='')
print(''''Agora conseguimos mudar valores, pois, diferente de uma 
TUPLA numa lista isso é possível\n''')
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print(f'\33[36m{valores}')
for pos, v in enumerate(valores):
    print(f'Na posição {pos} encontrei o valor {v}')
print('Fim da lista!\33[m')
