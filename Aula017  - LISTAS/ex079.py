valores = list()

while True:
    opc = ' '
    add = int(input('Digite um valor '))
    if add in valores:
        print('Valor já existe, não irei adicionar')
    else:
        valores.append(add)
        print('Adicionado com sucesso!')
    while opc not in 'SN':
        opc = input('Quer continuar? [S/N] ').upper().strip()[0]
    if opc == 'N':
        break
valores.sort()
print('_' * 30)
print(f'Você digitou os valores {valores}')
