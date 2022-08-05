def contagem(i, f, p):
    from time import sleep
    print('-=' * 20)
    if p == 0:
        p = 1
    p = abs(p)
    if f > i:
        ff = f + 1
    else:
        ff = f - 1
        p = p * -1
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')

    for c in range(i, ff, p):
        print(c, end=' ')
        sleep(0.25)
    print('Fim!')
    #print('-=' * 20)


contagem(1, 10, 1)
contagem(10, 0, 2)
print('\33[34mAgora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
print('\33[m')
contagem(i, f, p)
