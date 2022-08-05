n1 = int(input('Digite um número: '))
n2 = int(input('Agora mais um número '))
opc = 0

while opc == 0:
    while opc < 1 or opc > 5:
        opc = int(input('''Escolha uma opção: 
        [1] - Somar
        [2] - Multiplicar
        [3] - Maior
        [4] - Novos números
        [5] - Sair do programa
        Qual sua opção: '''))
        if 1 <= opc <= 5:
            print('')
        else:
            print('\n***** Preste atenção *****')
    if opc == 1:
        print(f'A soma é {n1 + n2}')
    elif opc == 2:
        print(f'O produto dos números é {n1 * n2}')
    elif opc == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n1 == n2:
            print('Não há maior, os valores são iguais')
        else:
            print(f'O maior número é {n2}')
    elif opc == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Agora mais um número '))
        opc = 0
    else:
        print('Fim')


