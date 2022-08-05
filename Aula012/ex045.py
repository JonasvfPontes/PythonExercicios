from random import randint
from time import sleep
print('Eu pensei em um objeto do JOKENPÔ')
pc = randint(1, 3)
op = int(input('''
Escolha uma opção abaixo e tente ganhar de mim ☻
1 - Pedra
2 - Papel
3 - Resoura
ESCOLHA: '''))
if op==0 or op>3:
    print('Vc é muito burro... Saia de perto de mim!')
else:
    lista = ['','pedra', 'papel', 'tesoura']
    pc = lista[pc]
    opc = lista[op]
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    print(f'''
Eu tinha pensado em {pc.upper()}
Vc escolheu         \33[;40m{opc.upper()}\33[m''')

    if pc == opc:
        print('\33[34mEMPATE\33[m')
    elif pc == 'pedra' and opc == 'papel':
        print('VC VENCEU!')
    elif pc == 'papel' and opc == 'Tesoura':
        print('VC VENCEU')
    elif pc == 'tesoura' and opc == 'pedra':
        print('VC VENCEU')
    else:
        print('\33[31mEu ganhei kkkkk\33[m')