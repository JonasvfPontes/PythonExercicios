n = 0
c = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {n} = {c*n}')
        c += 1
    print('-'*20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
