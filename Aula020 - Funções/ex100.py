from random import randint
from time import sleep

def sorteia(lst):

    print('Sorteado 5 valores da lista: ', end='')
    c = 0
    while c < 5:
        num = randint(1, 10)
        lst.append(num)
        c += 1
    for c in lst:
        print(c, end=' ')
        sleep(0.5)
    print('PRONTO!')


def somaPar(lts):
    sp = 0
    for c in lts:
        if c % 2 == 0:
            sp += c
    print(f'Somando os valores pares de {lts}, temos {sp}')


números = list()
sorteia(números)
somaPar(números)
