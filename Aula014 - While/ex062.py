print('='*5, 'PA', '='*5)
i = int(input('Digite um número '))
r = int(input('Qual a razão da PA '))
c = 0
opc =10
while opc != 0:
    while c < opc:
        print(i, end='→ ')
        i += r
        c += 1
    opc = int(input('\nVc quer ver mais quantos termos? '))
    c = 0
print('\nAcabou')