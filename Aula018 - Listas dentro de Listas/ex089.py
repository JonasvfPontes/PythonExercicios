from time import sleep
bd = [[], [[], []]]
while True:
    bd[0].append(input('Nome: ').capitalize().strip())
    bd[1][0].append(float(input('Nota 1: ')))
    bd[1][1].append(float(input('Nota 2: ')))
    opc = ' '
    while opc not in 'sn':
        opc = input('Quer continuar? [s/n] ').strip().lower()[0]
    if opc == 'n':
        break
print('\33[4:34m\nNº - NOME      -     MÉDIA\33[m')
for c in range(0, len(bd[0])):
    print(f'{c:<5}', end='')
    print(f'{bd[0][c]:<15}', end='')
    print(f'{(bd[1][0][c] + bd[1][1][c])/2:>5.2f}')
print('_' * 30)
while True:
    opc = int(input('\33[32mDeseja mostrar as notas de algum aluno? [\33[31mFim = 999\33[m]'))
    if opc == 999:
        sleep(1)
        print('FINALIZANDO...')
        sleep(1)
        print('Volte sempre!')
        break
    elif opc > len(bd[0]) - 1:
        print('\33[31mOpção inválida\33[m')
    else: #Quando o número é válido
        print(f'As notas de {bd[0][opc]} são {bd[1][0][opc]} e {bd[1][1][opc]}')
