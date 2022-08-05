def maior(* valores):
    from time import sleep
    m = 0
    cont = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for v in valores:
        print(v, end=' ')
        if v > m:
            m = v
        sleep(0.25)
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
