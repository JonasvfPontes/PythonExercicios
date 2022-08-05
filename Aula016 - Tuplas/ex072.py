extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
num = int(input('Digite um número entre 0 e 10: '))
while True:
    while 0 > num or num > 10:
        num = int(input('Novamente!\nDigite um número entre 0 e 10: '))
    print(f'O número {num} se escreve assim: {extenso[num]}')
    while True:
        opc = ' '
        opc = input('Quer continuar? [S/N] ').strip().upper()[0]
        if opc in 'SN':
            num = -1
            break
    if opc != 'S':
        break
print('Fim do programa!')
