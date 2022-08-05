from random import randint
vitórias = 0
print('=-' * 20)
print('VAMOS JOGAR PAR ou IMPAR?')
print('=-' * 20, '\n')
while True:
    pc = randint(0, 10)
    n = int(input('Diga um valor: '))
    opc = input('Você escolha PAR ou IMPAR? [P/I] ').strip()[0]
    #------------------------------------------------------------
    if opc in 'Pp': #Se o jogador escolher PAR
        if (pc + n) % 2 == 0: #E ganhar
            print('\33[32mVocê VENCEU!\33[m')
            print(f'Eu pensei em {pc} e vc escolheu {n}')
            vitórias += 1
            print('Vamos mais uma vez...')
        else:
            print('\33[31mVocê PERDEU!\33[m') #Ou perder
            print(f'GAME OVER! Você ganhou {vitórias}', 'vez' if vitórias == 1 else 'vezes')
            break
    elif opc in 'IiíÍ': #Se o jogador escolher IMPAR
        if (pc + n) % 2 != 0: #E ganhar
            print('\33[32mVocê VENCEU!\33[m')
            print(f'Eu pensei em {pc} e vc escolheu {n}')
            vitórias += 1
            print('Vamos mais uma vez...')
        else:
            print('\33[31mVocê PERDEU!\33[m') #Ou perder
            print(f'GAME OVER! Você ganhou {vitórias}', 'vez' if vitórias == 1 else 'vezes')
            break
    else:
        print('Vc deve escolher Par ou IMPAR... Vamos tentar de novo!')


